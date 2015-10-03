import os
import json

from collections import namedtuple
import gzip

from nfl.common import game_file_path, get_paths
from nfl.players import load_players
from nfl.schedule import get_latest_schedule
from nfl.grouped_stats import parse_grouped_stats
from nfl.drives import parse_drives

def get_game_data(game_center_path, game_id):
    file_path = game_file_path(game_center_path, game_id)
    with gzip.open(file_path) as f:
        data = f.read()
    return data


game_nt = namedtuple('game_nt', ['team_1', 'team_2'])
game_data_nt = namedtuple('game_data_nt', ['name', 'score', 'stats', 'home'])


def parse_game_file(game_center_path, game_id):
    raw_data = get_game_data(game_center_path, game_id)
    data = json.loads(raw_data)[game_id]
    assert data['qtr'] in ('Final', 'final overtime')

    home_data = {}
    home_data['name'] = data['home']['abbr']
    home_data['score'] = int(data['home']['score']['T'])
    home_data['stats'] = parse_grouped_stats(data['home']['stats'])
    home_data['home'] = True
    
    away_data = {}
    away_data['name'] = data['away']['abbr']
    away_data['score'] = int(data['away']['score']['T'])
    away_data['stats'] = parse_grouped_stats(data['away']['stats'])
    away_data['home'] = False

    game = game_nt(team_1=game_data_nt(**home_data), team_2=game_data_nt(**away_data))

    drives = parse_drives(data['drives'])
    return game


def load_week(game_center_path, schedule, week, year=2015, phase='REG'):
    matching_games = []
    for game in schedule.values():
        if (game['year'], game['season_type'], game['week']) == (year, phase, week):
            matching_games.append(game)
    return [parse_game_file(game_center_path, game['eid']) for game in matching_games]



