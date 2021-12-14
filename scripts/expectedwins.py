import pandas as pd

def get_expected_wins(df_rankings,df_schedule):
    #create two arrays to populate with data
    players = []
    expected_wins = []
    #loops through calculations for every player
    for index, row in df_schedule.iterrows():
        #get schedule in array to evaluate each game individually
        schedule = row['Schedule'].split('-')
        #grabs the rank for the player in question
        player_rank = df_rankings.loc[df_rankings['Name'] == row['Name'], 'Ranking']

        #calculates expected wins per game and adds to total
        wins = float(row['Wins'])
        for game in schedule:
            #grabs the opposition's rank
            opp_rank = df_rankings.loc[df_rankings['Name'] == game, 'Ranking']
            #calulated expected win and adds to total
            wins = float(wins) + (float(player_rank)/(float(player_rank) + float(opp_rank)))
        players.append(row['Name'])
        expected_wins.append(wins)
    #put arrays of data into a datafram, sort, then export
    data= {"Name": players, "ExpectedWins": expected_wins}
    df_final = pd.DataFrame(data)
    df_final.sort_values('ExpectedWins', inplace=True, ascending=False)
    print(df_final)
    df_final.to_csv('expectedwins.csv', index=False)
