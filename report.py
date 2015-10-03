#!/usr/bin/env python

import nfl.schedule
import nfl.update
import nfl.teams_matchups
import nfl.common

import os.path
from nfl.update import update

data_path = os.path.join(os.path.dirname(__file__), 'data')
schedule, paths = update(data_path)

y, p, w = nfl.schedule.current_nfl_week()
all_weeks_games = nfl.teams_matchups.previous_weeks_games(paths.gamecenter, schedule, w)

nfl.teams_matchups.print_overall_averages(all_weeks_games)

this_weeks_games = nfl.schedule.get_week_schedule(y, p, w)
for game in this_weeks_games:
    home = game['home']
    away = game['away']
    print("="*80)
    print("{} vs {}".format(home, away))
    print("record {}: ".format(home))
    nfl.teams_matchups.print_team_stats(all_weeks_games, home)
    print("record {}: ".format(away))
    nfl.teams_matchups.print_team_stats(all_weeks_games, away)
    
# Oposition average_points, averge conceded



# What is the best matchup
# What makes a good matchup, total points? Close game.

#Teams,
#Each vs Each
#Rushing yards, 
#Short throw
#Long Throw
#Turn overs
#Blocks
#Holding to 4th
#Rushing yards
#
#
#Players
#Snaps
#Numbr times targeted  (who else was on field, who was the QB).
#Postition when targeted. 
#Red zone targets
#Snaps
#Post Throw runs.
#Who was the recive against.