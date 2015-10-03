import nfl.parse_data
import nfl.schedule

team_stats = {}

def previous_weeks_games(game_center_path, schedule, current_week):
    all_weeks_games = []
    for w in range(1, current_week):
        games = nfl.parse_data.load_week(game_center_path, schedule, w)
        all_weeks_games.append(games)
    return all_weeks_games

def print_overall_averages(all_weeks_games):
    total_points = 0
    number_of_games = 0
    rushing_yards = 0
    passing_yards = 0
    for week_games in all_weeks_games:
        for game in week_games:
            number_of_games += 1
            for team in game:
                total_points += team.score
                passing_yards += team.stats.team.passing_yds
                rushing_yards += team.stats.team.rushing_yds

    print("Overall stats---")
    print("Average points: {:.2f}".format(float(total_points)/(2*number_of_games)))
    print("Average Rushing yards: {:.2f}".format(float(rushing_yards)/(2*number_of_games)))
    print("Average passing yards: {:.2f}".format(float(passing_yards)/(2*number_of_games)))

def get_teams_games(all_weeks_games, team):
    matching_games = []
    for week_games in all_weeks_games:
        for game in week_games:
            if team in (game.team_1.name, game.team_2.name):
                matching_games.append(game)
    return matching_games

def get_sides(games, team):
    us = []
    them = []
    for game in games:
        for side in game:
            if side.name == team:
                us.append(side)
            else:
                them.append(side)
    return us, them

from collections import namedtuple

team_stats = namedtuple('team_stats', ['scored', 'conceded', 'other_teams'])
stats = namedtuple('stats', ['points', 'passing_yards', 'rushing_yards'])

def get_side_stats(sides):
    average_points_scored = float(sum(s.score for s in sides))/len(sides)
    average_passing_yards = float(sum(s.stats.team.passing_yds for s in sides))/len(sides)
    average_rushing_yards = float(sum(s.stats.team.rushing_yds for s in sides))/len(sides)
    return stats(average_points_scored, average_passing_yards, average_rushing_yards)

def get_team_stats(all_weeks_games, team, exclude_team=None):
    games = get_teams_games(all_weeks_games, team)
    if exclude_team:
        games = [g for g in games if exclude_team not in (g.team_1.name, g.team_2.name)]
    us, them = get_sides(games, team)
    other_teams = [t.name for t in them]
    return team_stats(get_side_stats(us), get_side_stats(them), other_teams)

def print_team_stats(all_weeks_games, team):
    games = get_teams_games(all_weeks_games, team)
    
    print("\tprevious games---")
    for game in games:
        opposition = game.team_1.name if team != game.team_1.name else game.team_2.name
        op_stats = get_team_stats(all_weeks_games, opposition, exclude_team=team)
        print("\t\t {} {} : {} {}    ({}: avg_pts: +{} -{})".format(game.team_1.name, 
                                                                    game.team_1.score,
                                                                    game.team_2.name,
                                                                    game.team_2.score,
                                                                    opposition,
                                                                    op_stats.scored.points,
                                                                    op_stats.conceded.points
                                                                    )
              )
    
    us, them = get_sides(games, team)

    team_stats = get_team_stats(all_weeks_games, team)
    print("\tAverage points scored: {}".format(team_stats.scored.points))
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.conceded.points))
    print("\tAverage points conceded: {}".format(team_stats.conceded.points)) 
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.scored.points))
    print("\tAverage passing yards scored: {}".format(team_stats.scored.passing_yards))
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.conceded.passing_yards))
    print("\tAverage passing yards conceded: {}".format(team_stats.conceded.passing_yards)) 
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.scored.passing_yards))
    print("\tAverage rushing yards scored: {}".format(team_stats.scored.rushing_yards))
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.conceded.rushing_yards))
    print("\tAverage rushing yards conceded: {}".format(team_stats.conceded.rushing_yards)) 
    for oteam in team_stats.other_teams:
        oteam_stats = get_team_stats(all_weeks_games, oteam, exclude_team=team)
        print("\t\t {} {}".format(oteam, oteam_stats.scored.rushing_yards))

