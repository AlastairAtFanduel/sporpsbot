import nfl.common

def download_missing_games():
    schedule = get_latest_schedule()
    game_ids = schedule.keys()
    for game_id in game_ids:
        download_game(game_id)



def update(data_folder):
    paths = nfl.common.get_paths(data_folder)

    update_schedule(paths.schedule)
    paths.gamecenter


