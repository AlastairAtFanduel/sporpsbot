import os
import json

from collections import namedtuple
import gzip

from nfldata2.common import game_file_path
from nfldata2.players import load_players
from nfldata2.schedule import get_latest_schedule
from nfldata2.grouped_stats import parse_grouped_stats

PLAYERS = load_players()

def get_game_data(game_id):
    file_path = game_file_path(game_id)
    with gzip.open(file_path) as f:
        data = f.read()
    return data





def parse_game_file(game_id):
    raw_data = get_game_data(game_id)
    data = json.loads(raw_data)[game_id]

    home = self.data['home']['abbr']
    away = self.data['away']['abbr']

    home_score = int(self.data['home']['score']['T'])
    away_score = int(self.data['away']['score']['T'])

    home_stats = parse_grouped_stats(self.data['home']['stats'])
    away_stats = parse_grouped_stats(self.data['away']['stats'])

    drives = self.data['drives']
    for drive_id, drive_data in sorted(drives.items()):
        import pdb; pdb.set_trace()
        plays = drive_data['plays']
    
    play_events = data['players']  #?



    self.data['qtr']
    self.data['clock']




#data['2015092400']['drives']['1']['result']
#u'Safety'
#(Pdb) data['2015092400']['drives']['1']['start']
#{u'yrdln': u'WAS 19', u'team': u'WAS', u'qtr': 1, u'time': u'15:00'}
#(Pdb) data['2015092400']['drives']['1']['end']
#{u'yrdln': u'WAS 17', u'team': u'WAS', u'qtr': 1, u'time': u'12:47'}
#
#(Pdb) data['2015092400']['drives']['1']['postime']
#u'2:13'
#data['2015092400']['drives']['1']['numplays']
#7
#
#data['2015092400']['drives']['1']['penyds']
#
## first downs?
#(Pdb) data['2015092400']['drives']['1']['fds']
#0
#data['2015092400']['drives']['1']['ydsgained']
#8
#data['2015092400']['drives']['1']['plays'].keys()
#[u'159', u'57', u'35', u'195', u'137', u'102', u'81']


#---
# Team sats
#---




parse_game_file(2015092400)





    #game_flow:
    #    field_position
    #    time
    #    team in possesion
    #    possesion time
    #    game_clock
    #    a drive :)
    #    a play

    #def is_pregame(self):
    #    return self.qtr == 'Pregame'
 
    #def is_halftime(self):
    #    return self.qtr == 'Halftime'
 
    #def is_final(self):
    #    return 'final' in self.qtr.lower()



def _json_plays(drive, data):
    """
    Takes a single JSON drive entry (data) and converts it to a list
    of Play objects. This includes trying to resolve duplicate play
    conflicts by only taking the first instance of a play.
    """
    plays = []
    seen_ids = set()
    seen_desc = set()  # Sometimes duplicates have different play ids...
    for playid in map(str, sorted(map(int, data))):
        p = data[playid]
        desc = (p['desc'], p['time'], p['yrdln'], p['qtr'])
        if playid in seen_ids or desc in seen_desc:
            continue
        seen_ids.add(playid)
        seen_desc.add(desc)
        plays.append(Play(drive, playid, data[playid]))
    return plays

def _json_play_players(play, data):
    """
    Takes a single JSON play entry (data) and converts it to an OrderedDict
    of player statistics.

    play is the instance of Play that this data is part of. It is used
    to determine whether the player belong to the home team or not.
    """
    players = OrderedDict()
    for playerid, statcats in data.iteritems():
        if playerid == '0':
            continue
        for info in statcats:
            if info['statId'] not in nflgame.statmap.idmap:
                continue
            if playerid not in players:
                home = play.drive.game.is_home(info['clubcode'])
                if home:
                    team_name = play.drive.game.home
                else:
                    team_name = play.drive.game.away
                stats = nflgame.player.PlayPlayerStats(playerid,
                                                       info['playerName'],
                                                       home, team_name)
                players[playerid] = stats
            statvals = nflgame.statmap.values(info['statId'], info['yards'])
            players[playerid]._add_stats(statvals)
    return players


def _json_play_events(data):
    """
    Takes a single JSON play entry (data) and converts it to a list of events.
    """
    temp = list()
    for playerid, statcats in data.iteritems():
        for info in statcats:
            if info['statId'] not in nflgame.statmap.idmap:
                continue
            statvals = nflgame.statmap.values(info['statId'], info['yards'])
            statvals['playerid'] = None if playerid == '0' else playerid
            statvals['playername'] = info['playerName'] or None
            statvals['team'] = info['clubcode']
            temp.append((int(info['sequence']), statvals))
    return [t[1] for t in sorted(temp, key=lambda t: t[0])]

def _json_game_player_stats(game, data):
    """
    Parses the 'home' and 'away' team stats and returns an OrderedDict
    mapping player id to their total game statistics as instances of
    nflgame.player.GamePlayerStats.
    """
    players = OrderedDict()
    for team in ('home', 'away'):
        for category in nflgame.statmap.categories:
            if category not in data[team]['stats']:
                continue
            for pid, raw in data[team]['stats'][category].iteritems():
                stats = {}
                for k, v in raw.iteritems():
                    if k == 'name':
                        continue
                    stats['%s_%s' % (category, k)] = v
                if pid not in players:
                    home = team == 'home'
                    if home:
                        team_name = game.home
                    else:
                        team_name = game.away
                    players[pid] = nflgame.player.GamePlayerStats(pid,
                                                                  raw['name'],
                                                                  home,
                                                                  team_name)
                players[pid]._add_stats(stats)
    return players


def load_week(week, year=2015, phase='REG'):
    schedule = get_latest_schedule()

    matching_games = []
    for game in schedule.values:
        if (game.year, game.kind, game.week) == (year, phase, week):
            matching_games.append(game)

    return [parse_game_file(game.game_id) for game in matching_games]
