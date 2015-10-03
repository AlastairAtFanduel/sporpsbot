import os
import datetime
import urllib2
import gzip

import nfl.common

def after_game(game_id):
    year = int(game_id[:4])
    month = int(game_id[4:6])
    day = int(game_id[6:8])
    game_date = datetime.datetime(year, month, day)
    return (datetime.datetime.now() - game_date).days > 1

def download_games(gamecenter_path, game_ids):
    game_id_file_path_dict = {
                                os.path.basename(nfl.common.game_file_path(gamecenter_path, game_id)): game_id 
                                for game_id in game_ids
                             }
    file_paths = set(game_id_file_path_dict)
    known_games = set(os.listdir(gamecenter_path))
    files_to_download = sorted(file_paths - known_games)
    for file_to_download in files_to_download:
        game_id = game_id_file_path_dict[file_to_download]
        url = "http://www.nfl.com/liveupdate/game-center/{game_id}/{game_id}_gtd.json".format(game_id=game_id)
        try:
            data = urllib2.urlopen(url, timeout=5).read()
        except urllib2.HTTPError:
            print("Couldn't find game_id = '{}'".format(url))
            raise
        except socket.timeout:
            raise

        print("Writing file = {}".format(nfl.common.game_file_path(gamecenter_path, game_id)))
        with gzip.open(nfl.common.game_file_path(gamecenter_path, game_id), 'wb') as f:
            f.write(data)

    return files_to_download
