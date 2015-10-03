r = """

curl 'http://www.nfl.com/injuries?week=1' -H 'Host: www.nfl.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-GB,en;q=0.5' --compressed -H 'Referer: http://www.nfl.com/injuries?week=1' -H 'Cookie: mbox=PC#1442663334327-562365.21_22#1444170911|session#1442959630138-911641#1442963171|check#true#1442961371; s_pers=%20s_nr%3D1442663622649%7C1445255622649%3B%20s_lv%3D1442672072133%7C1537280072133%3B%20s_lv_s%3DLess%2520than%25201%2520day%7C1442673872133%3B%20s_lastvisit%3D1442959630879%7C1537567630879%3B%20s_fid%3D23D6E421681C613C-3BB1D0009E5E23E7%7C1506119711174%3B%20s_pv%3Dnfl%253Ainjuries%253Aweek%25201%7C1442963111175%3B%20p36%3Dna%257Chold%7C1600641311178%3B; s_vi=[CS]v1|2AFEA5D385313F96-60000105C001618A[CE]; __psrw=67d4783c-5ec4-11e5-87c9-22000b2108b8; nflsubs=eyeqwe|GAME_PASS; aamnfl=TEAM%3DSF%3BGPPS%3Dyes%3BEpsilon%3DIntlAll2015%3BGPConfirmFunnel%3DGPConfirmFunnel%3BGame%20Pass%20Prev%20Subscriber%3DNo%202014%3Bgp%3D2015subscriber; aam_sc=aamsc%3D513545%7C1886561; aam_did=65302377954571879403821307110813574289; _cb_ls=1; _chartbeat2=D8p_jH3N13ODsOJjI.1442663447762.1442961311448.1101; navigationTeamsDDOpen=true; __gads=ID=0574f43166f15937:T=1442663448:S=ALNI_MYr0DtMMZqn36bfIGEDJO65RKWhjw; headerSubProducts=nflNetworkOnlineClass%2CgamePassClass; __psord=3299038%7C; __tuuid=0a47ba88-2dd4-434f-8ba7-e4c0867265ff; _ga=GA1.2.1746328047.1442674044; ywandp=10002066517279%3A3600970498; fpc=10002066517279%3AZV-PDWRf%7C%7C; hpCpFrequencyCap=_ver=1.0.0&_an=%7B%22view%22%3A1%2C%22expiration%22%3A%222015-09-27T22%3A22%3A57.253Z%22%2C%22expires%22%3A%222015-12-19T22%3A22%3A57.253Z%22%2C%22expirationDay%22%3A7%7D; hpHtFrequencyCap=_ver=1.0.0&_an=%7B%22view%22%3A1%2C%22expiration%22%3A%222015-09-27T22%3A22%3A57.649Z%22%2C%22expires%22%3A%222015-12-19T22%3A22%3A57.649Z%22%2C%22expirationDay%22%3A7%7D; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3D-%3B%20s_sq%3D%3B; fsr.s=%7B%22v2%22%3A-2%2C%22v1%22%3A1%2C%22rid%22%3A%22d048012-57676153-0671-63a3-5874d%22%2C%22to%22%3A5%2C%22c%22%3A%22http%3A%2F%2Fwww.nfl.com%2Finjuries%22%2C%22pv%22%3A11%2C%22lc%22%3A%7B%22d1%22%3A%7B%22v%22%3A11%2C%22s%22%3Atrue%7D%7D%2C%22cd%22%3A1%2C%22f%22%3A1442960889248%2C%22sd%22%3A1%7D' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0'


1) Record who is injured.
2) Match up with game records.
3) Process player salaries from draftkkings.


POST https://api.nfl.com/v1/oauth/token
client_credentials
dyZHpNCWN5iuPx1gdbE3Dx9JAJIzZSCQ  # client id
abD8E45RS31lZIHZhqoev5Zr78JO8j4W  # client secert
813be36d-05c5-4922-a924-6d3db617a2e3 # device id


{"access_token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOiI4MTNiZTM2ZC0wNWM1LTQ5MjItYTkyNC02ZDNkYjYxN2EyZTMiLCJjbGllbnRJZCI6ImR5WkhwTkNXTjVpdVB4MWdkYkUzRHg5SkFKSXpaU0NRIiwiZXhwIjoxNDQyOTcwNTYzLCJpYXQiOjE0NDI5NjY5NjN9.3wxHwwpC290OFHm4yvxvzJs2oydZ_TiJrOnq6u_vuVs","token_type":"Bearer","expires_in":3600,"refresh_token":null,"scope":null}
Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOiI4MTNiZTM2ZC0wNWM1LTQ5MjItYTkyNC02ZDNkYjYxN2EyZTMiLCJjbGllbnRJZCI6ImR5WkhwTkNXTjVpdVB4MWdkYkUzRHg5SkFKSXpaU0NRIiwiZXhwIjoxNDQyOTcwNTAzLCJpYXQiOjE0NDI5NjY5MDN9.MSxIYwYjFhghaDIDoKDBAU2YEVGRxrEGRf8Kzld2xMg

https://api.nfl.com/docs/global/endpoints/index.html
curl --data "grant_type=client_credentials&client_id=dyZHpNCWN5iuPx1gdbE3Dx9JAJIzZSCQ&client_secret=abD8E45RS31lZIHZhqoev5Zr78JO8j4W"  'https://api.nfl.com/v1/oauth/token'
{"access_token":"eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOm51bGwsImNsaWVudElkIjoiZHlaSHBOQ1dONWl1UHgxZ2RiRTNEeDlKQUpJelpTQ1EiLCJleHAiOjE0NDI5NzA5OTAsImlhdCI6MTQ0Mjk2NzM5MH0.vNwy-N0AUH2cZrNQ3Mu2XMG-pRlGJVKmdhs58adYbkI","token_type":"Bearer","expires_in":3600,"refresh_token":null,"scope":null}



curl 'https://api.nfl.com/v1/teams/10040325-2015-4ddf-6e65-2af71b01cbf5' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOm51bGwsImNsaWVudElkIjoiZHlaSHBOQ1dONWl1UHgxZ2RiRTNEeDlKQUpJelpTQ1EiLCJleHAiOjE0NDI5NzEzMDYsImlhdCI6MTQ0Mjk2NzcwNn0.nNYXefXIjtK2LGiyYVfWjAyLFLkqFxj9zkt1_Mm23Qk"


How to get the ids
curl 'https://api.nfl.com/v1/teams?s={"$query":{"season":2015},"$take":40}&fs={id,season,fullName,nickName,abbr,teamType,conference{abbr},division{abbr}}' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOm51bGwsImNsaWVudElkIjoiZHlaSHBOQ1dONWl1UHgxZ2RiRTNEeDlKQUpJelpTQ1EiLCJleHAiOjE0NDI5NzEzMDYsImlhdCI6MTQ0Mjk2NzcwNn0.nNYXefXIjtK2LGiyYVfWjAyLFLkqFxj9zkt1_Mm23Qk" -g

How to get the injures
curl 'https://api.nfl.com/v1/teams/10041200-2015-ad43-5d9c-79ba50d47bd?s={"$query":{"season":2015},"$take":40}&fs={id,season,fullName,injuries,nickName,abbr,teamType,conference{abbr},division{abbr},injuries{id,type,person{firstName,lastName,},injury,injuryStatus,practice,practiceStatus,position,status}}' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6bnVsbCwiZGV2aWNlSWQiOm51bGwsImNsaWVudElkIjoiZHlaSHBOQ1dONWl1UHgxZ2RiRTNEeDlKQUpJelpTQ1EiLCJleHAiOjE0NDI5NzEzMDYsImlhdCI6MTQ0Mjk2NzcwNn0.nNYXefXIjtK2LGiyYVfWjAyLFLkqFxj9zkt1_Mm23Qk" -g | jq .


Get the rosters too.
"""
import datetime
import json
import os
import requests
from collections import namedtuple
from functools import partial
from collections import defaultdict
import nfl.common

INJURY_FOLDER = os.path.join(os.path.dirname(__file__), 'injury_data')
ROSTER_FOLDER = os.path.join(os.path.dirname(__file__), 'roster_data')
TEAMS_FOLDER = os.path.join(os.path.dirname(__file__), 'teams_data')

def dump_today(teams, injury, roster):
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


access_token = get_access_token()
week = get_current_week(access_token)
current_week = week['week']
teams = get_teams(access_token)
injuries = get_injures(access_token, teams, current_week)
rosters = get_rosters(access_token, teams, current_week)
dump_today(teams, injuries, rosters)