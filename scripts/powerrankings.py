import pandas as pd

def get_power_rankings(df_points):
    #get every players point differential
    df_points['PointDiff'] = df_points['PointsFor'] - df_points['PointsAgainst']

    #calculate the average point differential amoung players
    average = df_points['PointDiff'] / len(df_points.index)

    #calculate the distance to the average point differential for every player
    df_points['Distance'] = df_points['PointDiff'] - average

    #add the min distance to point differential to everyones score 
    #minus here is to account for the negitive
    df_points['DistanceAdj'] = df_points['Distance'] - df_points['Distance'].min()

    #calculating the average points score for every team each week
    sum = df_points['PointsFor'].sum()
    average_pf = (sum / df_points['Week'][0]) / len(df_points.index)
    df_points['DistanceAdj'] = df_points['DistanceAdj'] + average_pf

    #normalizing scores on a 0 to 100 scale
    df_points['Score'] = (df_points['DistanceAdj'] / df_points['DistanceAdj'].max()) * 100

    #order in first to last
    df_points.sort_values('Score', inplace=True, ascending=False)
    df_final = df_points.drop(columns=['PointsFor','PointsAgainst','Week','PointDiff','Distance','DistanceAdj'])
    df_final.to_csv('rankings.csv', index=False)

    print(df_final)