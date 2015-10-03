import nfl.common
import nfl.games
import nfl.injury
import nfl.schedule

def update(data_folder):
    paths = nfl.common.get_paths(data_folder)

    print("Parsing schedule")
    schedule = nfl.schedule.get_latest_schedule(paths.schedule)

    print("Downloading latest games")
    nfl.games.download_missing_games(paths.gamecenter, schedule)

    print("Updating injures")
    nfl.injury.update_injures(paths)

    return schedule, paths


