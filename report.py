#!/usr/bin/env python

import nfl.schedule
import nfl.update

nfl.schedule.download_missing_games(game_center_path)

y, p, w = nfl.schedule.current_nfl_week()
all_weeks_games = previous_weeks_games(w)

print_overall_averages(all_weeks_games)

this_weeks_games = nfl.schedule.get_week_schedule(y, p, w)
for game in this_weeks_games:
    home = game['home']
    away = game['away']
    print("="*80)
    print("{} vs {}".format(home, away))
    print("record {}: ".format(home))
    print_team_stats(home)
    print("record {}: ".format(away))
    print_team_stats(away)
    
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