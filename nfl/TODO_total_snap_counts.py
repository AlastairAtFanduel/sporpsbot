import os
import csv
from collections import namedtuple, Counter, defaultdict

def parse_file(csv_file_path):
    with open(csv_file_path) as f:
        players = list(csv.DictReader(f))
        for player in players:
            player_number, player_name = player['Player'].split('-')
            yield player_name.split('.')[-1], int(player['Total Snaps']), player['Position']

files = [x for x in os.listdir('.') if x.endswith('csv')]

def make_counter():
    return Counter()
overall = defaultdict(make_counter)
for f in files:
    players = parse_file(f)
    for player_name, count, pos in players:
        overall[pos][player_name] += count


import pprint
for pos, players in overall.items():
    print('POSITION={}'.format(pos))
    pprint.pprint(sorted(players.items(), key=lambda x: x[1], reverse=True))
