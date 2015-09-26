from collections import namedtuple

import nflgame

game_nt = namedtuple('game_nt', ['home', 'away'])
game_data_nt = namedtuple('game_data_nt', ['name', 'score', 'stats', 'players'])
side_stats_fields = ['first_downs', 'total_yds', 'passing_yds', 'rushing_yds', 'penalty_cnt', 'penalty_yds', 'turnovers', 'punt_cnt', 'punt_yds', 'punt_avg']
side_stats = namedtuple('side_stats', side_stats_fields + ['total_seconds'])

player_stats_fields = [
                       'rushing_att',   # Rush attemp
                       'rushing_tds',   # Rush total yards
                       'rushing_yds',   # Total yards
            

                       # QB
                       'passing_att',    # attemnpt
                       'passing_yds',    # total yards
                       'passing_cmp',    #
                       'passing_incmp',  # in complete pass
                       'passing_int',    # Missed pass
                       'passing_tds',    # touch downs
                       'passing_sk',     # sacks
                       'passing_sk_yds'  # yards lost

                       
                       'receiving_tds',

                       'receiving_rec',   # Got the ball
                       'receiving_yds',   # Total pass reception yards
                       'receiving_tds',   # touch down



                       'receiving_tar',         'player was a target'
                       'passing_cmp_air_yds',   'complete pass length, completion no including reciver run'
                       'passing_incmp_air_yds', 'incomplete pass length, completion no including reciver run'
                       'receiving_yac_yds',     'yards gained after the pass' 
                       'defense_tkl_loss',      'player tackeled for a loss of yardage'


                       #'receiving_twopta',      # attempt
                       #'receiving_twoptm',      # got it
                       #'receiving_twoptmissed', # missed
                       #'passing_twopta',        # attempt
                       #'passing_twoptm',        # got it
                       #'passing_twoptmissed',   # missed
                       #'rushing_twopta',        # attempt
                       #'rushing_twoptm',        # got it
                       #'rushing_twoptmissed',   # missed
                       #'fumbles_trcv',
                       #'fumbles_tot',
                       #'fumbles_rcv',
                       #'fumbles_yds',
                       #'fumbles_lost',
                       #'kicking_fga',      # field goal kick attempt
                       #'kicking_fgm',      # field goal kick made
                       #'kicking_fgmissed', # field goal kick missed
                       #'kicking_fgb',      # field goal blocked
                       #'kicking_xpa',       # one_point kick attempt
                       #'kicking_xpmade',    # one_point kick made
                       #'kicking_xpmissed',  # one_point kick  missed
                       #'kicking_xpb',       # one_point kick  one point blocked

                       #???? 'rushing_lng',
                       #???? 'receiving_lng',
                       #???? 'rushing_lngtd',
                       #???? 'receiving_lngtd',
                      ]

player_stats_nt = namedtuple('player_stats_nt', )



def generate_side_stats(stats):
    data = {}
    data = {
        field:getattr(field, game.stats_home for field in side_stats_fields
    }
    data['total_seconds'] = game.stats_home.pos_time.total_seconds()


games = nflgame.games(2015, week=1)
for game_data in games:

    all_players = [p for p in game_data.players]
    home_players = [p for p in all_players if p.home]
    away_players = [p for p in all_players if p.away]

    x.name
    x.team
    x.stats

    home_data = {}
    home_data['name'] = game_data.home
    home_data['score'] = game_data.score_home
    home_stats_dict = generate_side_stats(game.stats_home)
    home_data['stats'] = side_stats(**home_stats_dict)
    
    away_data = {}
    away_data['name'] = game.away
    away_data['score'] = game.score_away
    away_stats_dict = generate_side_stats(game.stats_home)
    away_data['stats'] = side_stats(**away_stats_dict)

    game = game_nt(home=game_data_nt(*home_data*), away=game_data_nt(**away_data))


        



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