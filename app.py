import pandas as pd
from scripts.powerrankings import get_power_rankings

points = pd.read_csv('points.csv')
get_power_rankings(points)
