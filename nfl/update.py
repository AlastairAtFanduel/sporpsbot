import nfl.common
import nfl.games

def download_missing_games(gamecenter_path, schedule):
    game_ids = schedule.keys()
    past_games = [gid for gid in game_ids if nfl.games.after_game(gid)]
    download_games(gamecenter_path, past_games)

def update(data_folder):
    paths = nfl.common.get_paths(data_folder)

    print("Parsing schedule")
    schedule = get_latest_schedule(paths.schedule)
    print("Downloading latest games")
    download_missing_games(paths.gamecenter, schedule)


