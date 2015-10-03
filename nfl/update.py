import nfl.common
import nfl.games
import nfl.injury
import nfl.schedule

def download_missing_games(gamecenter_path, schedule):
    game_ids = schedule.keys()
    past_games = [gid for gid in game_ids if nfl.games.after_game(gid)]
    nfl.games.download_games(gamecenter_path, past_games)

def update(data_folder):
    paths = nfl.common.get_paths(data_folder)

    print("Parsing schedule")
    schedule = nfl.schedule.get_latest_schedule(paths.schedule)

    print("Downloading latest games")
    download_missing_games(paths.gamecenter, schedule)

    print("Updating injures")
    nfl.injury.update_injures(paths)


