"""Teams


Each american football team is 3 teams.

For each aspect of the game
x def vs x off running yards 7, off 13 goes
x off vs y def running yards 15, off 7 goes.
x special vs y special running yards 7
But there is more.

Two factors Dominance vs effectivness.


Teams

Need to record
x def vs y off how many goes does y off get before score   (idicator that team is outmatched)
x def vs y off how many goes does y off get before turnover/4th down (reverse)

How many attack sequence did they get.  Like above but not effected by turn overs.
Turnovers give points to def and their attack they get a new attack sequence.
Calculate number of ecpected attack sequences per team.

Player results per attack sequence.

Need to predict
x def vs y off how many td do they give up. (turnovers)
x spec vs y spec how many points do they give up
y off vs x def (passing yards, running yards etc)
"""
from collections import defaultdict, namedtuple


class Team():
    def __init__(self, name):
        self.name = name


class Teams():
    def __init__(self):
        self.teams = {}    # 3 code to team model.
        self.passing_yards = PlainAverages("passing_yards")

Result = namedtuple("Result", ["team_a", "team_b", "value"])

# Each team a score and an uncertanty.

class PlainDoubleAverages():
    def __init__(self, name):
        self.name = name
        self.teams_a = defaultdict(list)
        self.teams_b = defaultdict(list)
        self.average = None

    def record_results(self, results):
        for result in results:
            self.record_result(result)

    def record_result(self, result):
        team_a = result.team_a
        team_b = result.team_b
        value = result.value

        if self.average is None:

        half_scores_a = self.teams_a.get(team_a, [0])
        half_scores_b = self.teams_b.get(team_b, [0])

        pred_a = sum(half_scores_a)/len(half_scores_a)
        pred_b = sum(half_scores_b)/len(half_scores_b)

        prediction = pred_a + pred_b
        half_diff = (prediction - value)/2
        self.teams_a[team_a].append(pred_a - half_diff)
        self.teams_b[team_b].append(pred_b - half_diff)

    def average(self):
        return calc_avg(self.teams_a) + calc_avg(self.teams_b)


    def calc_avg(self, teams):
        if teams:
            return sum(teams.values())/len(teams)
        else:
            return 0

    def predict(self, team_a, team_b):
        pass        



# Plain averages
# Home and away
# Propotional
# Links persevered and effected.
# Depends on how long ago more recent matches more effected.
# Binomal distrubition.


Def Off have a binonmal distrubution.

We can follow all Links
20x 30y 15z

We know our average.  We know the avaerage avaerge.  Each opp kinows their average.