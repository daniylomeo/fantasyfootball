import pandas as pd
from scripts.powerrankings import get_power_rankings
from scripts.expectedwins import get_expected_wins

#grab power rankings
points = pd.read_csv('points.csv')
get_power_rankings(points)

# #get expected wins
# rankings = pd.read_csv('rankings.csv')
# schedule = pd.read_csv('schedule.csv')
# get_expected_wins(rankings,schedule)