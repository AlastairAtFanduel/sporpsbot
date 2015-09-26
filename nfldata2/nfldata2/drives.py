#List of plays
#List of drives


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


    #game_flow:
    #    field_position
    #    time
    #    team in possesion
    #    possesion time
    #    game_clock
    #    a drive :)
    #    a play


def parse_drives(drive_data):
    for drive_id, drive_data in sorted(drives.items()):
        import pdb; pdb.set_trace()
        plays = drive_data['plays']
    
    play_events = data['players']  #?

def parse_play(play):
    pass
