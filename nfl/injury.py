import datetime
import json
import os
import requests
from collections import namedtuple
from functools import partial
from collections import defaultdict
import nfl.common


def dump_today(paths, teams, injury, roster):
    file_name = "{}.json".format(datetime.date.today().isoformat())

    teams_file = os.path.join(TEAMS_FOLDER, file_name)
    with open(teams_file, 'w') as tfile:
        json.dump(teams, tfile, indent=4, separators=(',', ': '))

    injury_file = os.path.join(INJURY_FOLDER, file_name)
    with open(injury_file, 'w') as ifile:
        json.dump(injury, ifile, indent=4, separators=(',', ': '))

    roster_file = os.path.join(ROSTER_FOLDER, file_name)
    with open(roster_file, 'w') as rfile:
        json.dump(roster, rfile, indent=4, separators=(',', ': '))

def get_access_token():
    playload = {"grant_type": "client_credentials",
                "client_id": "dyZHpNCWN5iuPx1gdbE3Dx9JAJIzZSCQ",
                "client_secret": "abD8E45RS31lZIHZhqoev5Zr78JO8j4W"
                }
    r = requests.post('https://api.nfl.com/v1/oauth/token', params=playload)
    res = r.json()

    access_token = res['access_token']
    return access_token


team_mapping = {
                'conference': ('conference', None),
                'division': ('division', None),
                'season': ('season', None),
                'type': ('teamType', None),
                'abbr': ('abbr', None),
                'fullname': ('fullName', None),
                'nickname': ('nickName', None),
                'id': ('id', None)
                }
team_nt = namedtuple('team_nt', team_mapping.keys())



player_injury_mapping = {'status', 
                         'practiceStatus',
                         'practice',
                         'person',
                         'injuryStatus',
                         'position',
                         'injury',
                         'type',
                         'id'
                         }


def get_data(access_token, url):
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }
    raw_data = requests.get(url, headers=headers)
    data = raw_data.json()
    return data


def get_teams(access_token):
    query = '{"$query":{"season":2015}}&fs={id,season,fullName,nickName,abbr,teamType,conference{abbr},division{abbr}}'
    url = 'https://api.nfl.com/v1/teams?s={}'.format(query)
    teams = get_data(access_token, url)

    return [nfl.common.mapping_parse(team_mapping, team_nt, team) for team in teams['data']]

def get_current_week(access_token):
    url = 'https://api.nfl.com/v1/currentWeek?fs={name,week,seasonType,seasonTypeOrder,season}'
    current_week = get_data(access_token, url)
    #{u'week': 3, u'season': 2015, u'seasonTypeOrder': None, u'seasonType': u'REG', u'name': u'Week 3'}
    return current_week

def get_team_roster(access_token, team_id, current_week):
    depth_txt = 'depthChart{person{id,firstName,lastName},unit,depthOrder,positionAbbr}'
    roster_txt = 'roster{ week, id,firstName,lastName,displayName,birthDate}'
    fields_selection = 'fs={{id,season,fullName,nickName,abbr,{},{}}}'.format(depth_txt, roster_txt)


    query = 's={{"$query":{{"season":2015,"week": {}}}}}'.format(current_week)
    injury_query = '&'.join([query, fields_selection])
    url = 'https://api.nfl.com/v1/teams/{}?{}'.format(team_id, injury_query)
    team_roster = get_data(access_token, url)
    return team_roster

def get_team_injuries(access_token, team_id, current_week):
    injures_txt = 'injuries{id,type,person{firstName,lastName,id},injury,injuryStatus,practice,practiceStatus,status}'
    depth_txt = 'depthChart{person{id,firstName,lastName},unit,depthOrder,positionAbbr}'
    stats_txt = '' #regTeamSeasonStats{gamesPlayed,teamStats{passing}}'
    fields_selection = 'fs={{id,season,fullName,nickName,abbr,{},{},{}}}'.format(injures_txt,depth_txt, stats_txt)

    query = 's={{"$query":{{"season":2015,"week": {}}}}}'.format(current_week)
    injury_query = '&'.join([query, fields_selection])
    url = 'https://api.nfl.com/v1/teams/{}?{}'.format(team_id, injury_query)
    team_injuries = get_data(access_token, url)
    import pdb; pdb.set_trace()
    return team_injuries


def get_rosters(access_token, teams, current_week):
    rosters = defaultdict(list)
    for team in teams:
        team_roster = get_team_roster(access_token, team.id, current_week)
        rosters[team.id] = team_roster
    return rosters

def get_injures(access_token, teams, current_week):
    injuries = defaultdict(list)
    for team in teams:
        team_injuries = get_team_injuries(access_token, team.id, current_week)
        injuries[team.id] = team_injuries
    return injuries

def update_injures(paths):
    access_token = get_access_token()
    week = get_current_week(access_token)
    current_week = week['week']
    teams = get_teams(access_token)
    injuries = get_injures(access_token, teams, current_week)
    rosters = get_rosters(access_token, teams, current_week)
    dump_today(paths, teams, injuries, rosters)