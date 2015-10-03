import urllib2
import xml.dom.minidom as xml
import time
import datetime
from collections import OrderedDict
import gzip
import json
import os.path
from nfl.common import game_file_path

CUR_SCHEDULE = "http://www.nfl.com/liveupdate/scorestrip/ss.xml"

def current_nfl_week():
    dom = xml.parse(urllib2.urlopen(CUR_SCHEDULE, timeout=5))
    gms = dom.getElementsByTagName('gms')[0]
    current_week = int(gms.getAttribute('w'))
    current_year = int(gms.getAttribute('y'))

    phase = gms.getAttribute('t').strip()
    if phase == 'P':
        current_season_phase = 'PRE'
    elif phase == 'POST' or phase == 'PRO':
        current_season_phase = 'POST'
        current_week -= 17
    else:
        current_season_phase = 'REG'
    return current_year, current_season_phase, current_week

def schedule_url(year, stype, week):
    """
    Returns the NFL.com XML schedule URL. `year` should be an
    integer, `stype` should be one of the strings `PRE`, `REG` or
    `POST`, and `gsis_week` should be a value in the range
    `[0, 17]`.
    """
    xmlurl = 'http://www.nfl.com/ajax/scorestrip?'
    if stype == 'POST':
        week += 17
        if week == 21:  # NFL.com you so silly
            week += 1
    return '%sseason=%d&seasonType=%s&week=%d' % (xmlurl, year, stype, week)

def yield_weeks_until(end_year, end_phase, end_week):
    season_types = (
        ('PRE', xrange(0, 4 + 1)),
        ('REG', xrange(1, 17 + 1)),
        ('POST', xrange(1, 4 + 1)),
    )
    for year in range(2009, end_year+1):
        for phase, weeks in season_types:
            for week in weeks:
                yield year, phase, week
                if (end_year, end_phase, end_week) == (year, phase, week):
                    break


def parse_schedule(raw_schedule=None):
    if raw_schedule is None:
        raw_schedule = {}

    schedule = OrderedDict()
    for game_id, info in raw_schedule.get('games', []):
        schedule[game_id] = info

    last_updated = datetime.datetime.utcfromtimestamp(raw_schedule.get('time', 0))
    return schedule, last_updated


def update_schedule_file(schedule_file_path, schedule):
    with open(schedule_file_path, 'w') as jsonf:
        json.dump({'time': time.time(), 'games': sorted(schedule.items())},
                  jsonf,
                  indent=1,
                  sort_keys=True,
                  separators=(',', ': '))


def update_schedule(schedule):
    # Give a blank schedule to to rewrite
    known_weeks = set()
    for game_id, schedule_data in schedule.items():
        week = schedule_data['week']
        year = schedule_data['year']
        phase = schedule_data['season_type']
        known_weeks.add((year, phase, week))

    year, phase, week = current_nfl_week()
    for year, phase, week in yield_weeks_until(year, phase, week):
        if (year, phase, week) not in known_weeks:
            games = get_week_schedule(year, phase, week)
            for game in games:
                game_id = game['game_id']
                schedule[game_id] = game
    return schedule

def get_week_schedule(year, stype, week):
    """
    Returns a list of dictionaries with information about each game in
    the week specified. The games are ordered by gsis_id. `year` should
    be an integer, `stype` should be one of the strings `PRE`, `REG` or
    `POST`, and `gsis_week` should be a value in the range `[1, 17]`.
    """
    url = schedule_url(year, stype, week)
    try:
        print("loading url = '{}'".format(url))
        data = urllib2.urlopen(url)
        dom = xml.parse(data)
    except urllib2.HTTPError:
        raise IOError("Couldn't load {}".format(url))

    games = []
    for g in dom.getElementsByTagName("g"):
        gsis_id = g.getAttribute('eid')
        games.append({
            'game_id': gsis_id,
            'wday': g.getAttribute('d'),
            'year': year,
            'month': int(gsis_id[4:6]),
            'day': int(gsis_id[6:8]),
            'time': g.getAttribute('t'),
            'season_type': stype,
            'week': week,
            'home': g.getAttribute('h'),
            'away': g.getAttribute('v'),
            'gamekey': g.getAttribute('gsis'),
        })
    return games

def get_latest_schedule(sched_json_file):
    # Delete the file to rebuild
    # In future could check for differences
    with open(sched_json_file) as jsonf:
        try:
            raw_data = json.loads(jsonf.read())
        except IOError:
            print("File doesn't exist rebuilding")
            raw_data = None

    schedule, last_updated = parse_schedule(raw_data)

    current_time = datetime.datetime.utcnow()
    if (current_time - last_updated).days > 1:
        schedule = update_schedule(schedule)
        update_schedule_file(sched_json_file, schedule)

    return schedule
