x ="""Players

Initial objectives:
Internal player rankings.  
    How does coach x field/use player x.
    If Y is injured who will be brought in
    propotion of throws wr vs other wr with uncertainity

For each player how much involment is forcast
How many points would ech player get in game x ( Variance too.) Graphs
Some players may be 50/50.  Play not Play
"""
import json
import os

PLAYER_JSON_FILE = os.path.join(os.path.dirname(__file__), 'players.json')


class Player(object):
    """
    Player instances represent meta information about a single player.
    This information includes name, team, position, status, height,
    weight, college, jersey number, birth date, years, pro, etc.

    Player information is populated from NFL.com profile pages.
    """
    def __init__(self, data):
        self.player_id = data['gsis_id']
        self.gsis_name = data.get('gsis_name', '')
        self.full_name = data.get('full_name', '')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        self.team = data.get('team', '')
        self.position = data.get('position', '')
        self.profile_id = data.get('profile_id', 0)
        self.profile_url = data.get('profile_url', '')
        self.uniform_number = data.get('number', 0)
        self.birthdate = data.get('birthdate', '')
        self.college = data.get('college', '')
        self.height = data.get('height', '')
        self.weight = data.get('weight', '')
        self.years_pro = data.get('years_pro', 0)
        self.status = data.get('status', '')


def load_players():
    with open(PLAYER_JSON_FILE) as f:
        players = json.loads(f.read())
    return [Player(p) for pid, p in players.iteritems()]
