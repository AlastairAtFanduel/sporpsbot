import os
import json

from collections import namedtuple
import gzip

from nfldata2.common import game_file_path
from nfldata2.players import load_players
from nfldata2.schedule import get_latest_schedule
from nfldata2.grouped_stats import parse_grouped_stats
from nfldata2.drives import parse_drives

PLAYERS = load_players()

def get_game_data(game_id):
    file_path = game_file_path(game_id)
    with gzip.open(file_path) as f:
        data = f.read()
    return data


game_nt = namedtuple('game_nt', ['home', 'away'])
game_data_nt = namedtuple('game_data_nt', ['name', 'score', 'stats'])


def parse_game_file(game_id):
    raw_data = get_game_data(game_id)
    data = json.loads(raw_data)[game_id]

    assert self.data['qtr'] == 'Final'

    home_data = {}
    home_data['name'] = self.data['home']['abbr']
    home_data['score'] = int(self.data['home']['score']['T'])
    home_stats_dict = generate_side_stats(game.stats_home)
    home_data['stats'] = parse_grouped_stats(self.data['home']['stats'])
    
    away_data = {}
    away_data['name'] = self.data['away']['abbr']
    away_data['score'] = int(self.data['away']['score']['T'])
    away_stats_dict = generate_side_stats(game.stats_home)
    away_data['stats'] = parse_grouped_stats(self.data['away']['stats'])

    game = game_nt(home=game_data_nt(*home_data*), away=game_data_nt(**away_data))


    raw_drives = self.data['drives']
    drives = parse_drives(raw_drives)


def load_week(week, year=2015, phase='REG'):
    schedule = get_latest_schedule()

    matching_games = []
    for game in schedule.values:
        if (game.year, game.kind, game.week) == (year, phase, week):
            matching_games.append(game)

    return [parse_game_file(game.game_id) for game in matching_games]


parse_game_file(2015092400)



