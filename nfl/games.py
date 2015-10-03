import datetime

def after_game(game_id):
    year = game_id[:4]
    month = game_id[4:6]
    day = game_id[6:8]
    game_date = datetime.datetime(year, month, day)
    return datetime.datetime.now() - game_date > 1:

def download_game(game_id):
    if not after_game(game_id):
        print("Not after game", game_id)
        return None

    file_path = game_file_path(game_id)
    if not os.path.exists(file_path):
        url = "http://www.nfl.com/liveupdate/game-center/{game_id}/{game_id}_gtd.json".format(game_id=game_id)
        try:
            data = urllib2.urlopen(url, timeout=5).read()
        except urllib2.HTTPError:
            print("Couldn't find game_id = '{}'".format(url))
            return
        except socket.timeout:
            raise

        print("Writing file = {}".format(file_path))
        with gzip.open(file_path, 'wb') as f:
            f.write(data)

    return file_path

