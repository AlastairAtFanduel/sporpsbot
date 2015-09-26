
import csv
from collections import namedtuple

DK_FIELDS = ['Position', 'Name', 'Salary', 'GameInfo', 'AvgPointsPerGame', 'teamAbbrev']

dk_fields = ['pos', 'name', 'salary', 'team', 'game', 'avg_pts']
dk_player_nt = namedtuple('dk_player_nt', dk_fields)


def parse_file(csv_file_path):
    with open(csv_file_path) as f:
        salary_reader = csv.DictReader(f)
        for p in salary_reader:
            player = dk_player_nt(pos=p['Position'],
                                  name=p['Name'],
                                  salary=float(p['Salary']),
                                  team=p['teamAbbrev'],
                                  game=p['GameInfo'],
                                  avg_pts=float(p['AvgPointsPerGame'])
                                 )

            yield player

