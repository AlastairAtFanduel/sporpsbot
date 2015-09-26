from functools import partial

def parse_dataset_with_player_id(cls, data):   # Could map the data here
    parsed_data = []
    for players_id, data_dict in data:
        obj = cls(player_id=player_id, **data_dict)
        parsed_data.append(obj)
    return parsed_data

#---
# Kick ret stats
#---
kickret_stats_flds = ['player_id', 'name', 'ret', 'tds', 'lng', 'avg', 'lngtd']
kickret_stats_nt = namedtuple('kickret_stats_nt', kickret_stats_flds)
parse_kick_return_stats = partial(parse_dataset_with_player_id, kickret_stats_nt)

#---
# defense
#---
defense_stats_flds = ['player_id', 'name', 'ast', 'int', 'tkl', 'sk', 'ffum']
defense_stats_nt = namedtuple('defense_stats_nt', defense_stats_flds)
parse_defense_stats = partial(parse_dataset_with_player_id, defense_stats_nt)

#---
# fumbles
#---
fumbles_stats_flds = ['player_id', 'name', 'lost', 'trcv', 'rcv', 'tot', 'yds']
fumbles_stats_nt = namedtuple('fumbles_stats_nt', fumbles_stats_flds)
parse_fumble_stats = partial(parse_dataset_with_player_id, fumbles_stats_nt)

#---
# kicking
#---
kicking_stats_flds = ['player_id', 'xptot', 'name', 'totpfg', 'xpmade',
                      'xpa', 'fgm', 'xpmissed', 'fgyds', 'xpb', 'fga']
kicking_stats_nt = namedtuple('kicking_stats_nt', kicking_stats_flds)
parse_kicking_stats = partial(parse_dataset_with_player_id, kicking_stats_nt)

#---
# punt return
#---
punt_ret_flds = ['player_id', 'name', 'ret', 'tds', 'lng', 'avg', 'lngtd']
punt_ret_stats_nt = namedtuple('punt_ret_stats_nt', punt_ret_flds)
parse_puntret_stats = partial(parse_dataset_with_player_id, punt_ret_stats_nt)


#---
# Team stats
#---
team_stats_fields = ['first_downs',
                     'total_yds',
                     'passing_yds',
                     'rushing_yds',
                     'penalty_cnt',
                     'penalty_yds',
                     'turnovers',
                     'punt_cnt',
                     'punt_yds',
                     'punt_avg',
                     'pos_time']
team_stats_nt = namedtuple('team_stats_nt', team_stats_fields)

def parse_team_stats(data):
    """
    Takes a team stats JSON entry and converts it to a TeamStats namedtuple.
    """
    return team_stats_nt(
        first_downs=int(data['totfd']),
        total_yds=int(data['totyds']),
        passing_yds=int(data['pyds']),
        rushing_yds=int(data['ryds']),
        penalty_cnt=int(data['pen']),
        penalty_yds=int(data['penyds']),
        turnovers=int(data['trnovr']),
        punt_cnt=int(data['pt']),
        punt_yds=int(data['ptyds']),
        punt_avg=int(data['ptavg']),
        pos_time=PossessionTime(data['top']))

#---
# passing stats
#--- 
passing_stats_flds = ['player_id', 'twoptm', 'name', 'twopta', 'att', 'ints', 'tds', 'yds', 'cmp']
passing_stats_nt = namedtuple('passing_stats_nt', passing_stats_flds)
parse_passing_stats = partial(parse_dataset_with_player_id, passing_stats_nt)

#---
# Receiving stats
#---
receiving_stats_flds = ['player_id', 'name', 'twopta', 'tds', 'rec', 'lng', 'lngtd', 'yds', 'twoptm']
receiving_stats_nt = namedtuple('passing_stats_nt', receiving_stats_flds)
parse_receiving_stats = partial(parse_dataset_with_player_id, receiving_stats_nt)

#---
# rushing stats
#---
rushing_stats_flds = ['player_id', 'name', 'twopta', 'att', 'tds', 'lng', 'lngtd', 'yds', 'twoptm']
rushing_stats_nt = namedtuple('rushing_stats_nt', rushing_stats_flds)
parse_rushing_stats = partial(parse_dataset_with_player_id, rushing_stats_nt)

#---
# punting stats
#---
punting_stats_flds = ['player_id', 'name', 'i20', 'lng', 'avg', 'pts', 'yds']
punting_stats_nt = namedtuple('punting_stats_nt', punting_stats_flds)
parse_punting_stats = partial(parse_dataset_with_player_id, passing_stats_nt)


grouped_stats_map = [('kickret', parse_kick_return_stats), 
                      ('defense', parse_defense_stats),
                      ('fumbles', parse_fumble_stats), 
                      ('kicking', parse_kicking_stats), 
                      ('puntret', parse_puntret_stats, 
                      ('team', parse_team_stats), 
                      ('passing', parse_passing_stats), 
                      ('receiving', parse_receiving_stats), 
                      ('rushing', parse_rushing_stats), 
                      ('punting', parse_punting_stats)]
grouped_stats_nt = namedtuple('grouped_stats', grouped_stats_map.keys())

def parse_grouped_stats(grouped_stats):
    parsed_data_dict = {fld: parser(fld) for fld, parser in grouped_stats_map.items()}
    grouped_stats = grouped_stats_nt(**parsed_data_dict)
    return grouped_stats