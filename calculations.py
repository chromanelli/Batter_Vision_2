import pandas as pd
import os
from config import Config

def make_dicts():
    pitcher_df = pd.read_csv("data/pitcher_data.csv")
    batter_df = pd.read_csv("data/batter_data.csv")

    pitcher_ids = pitcher_df["player_id"].unique()
    pitcher_dict = {}
    for id in pitcher_ids:
        pitcher_dict[int(id)] = pitcher_df[pitcher_df["player_id"] == id]
    
    team_ids = batter_df["team_name_alt"].unique()
    team_dict = {}
    for id in team_ids:
        team_dict[id] = batter_df[batter_df["team_name_alt"] == id]
    
    return pitcher_dict, team_dict

def save_data(pitcher_best, batter_dfs):
    pitcher_id = str(pitcher_best["player_id"].values[0])
    batting_team = str(batter_dfs[0]["team_name_alt"].values[0])
    dirName = "data/" + str(Config.end_date) + "_" + pitcher_id + "_" + batting_team
    
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    
    pitcher_file = dirName + "/pitcher_best.csv"
    pitcher_best.to_csv(pitcher_file)

    for df in batter_dfs:
        pitchName = str(df["pitch_name"].values[0])
        fileName = dirName + "/" + batting_team + "_vs_" + pitchName + ".csv"
        df.to_csv(fileName)
        print()

    return

def calculate():
    pitcher_dict, team_dict = make_dicts()
    
    pitcher_df = pitcher_dict[Config.pitcher]
    pitcher_most_used = pitcher_df.nlargest(2, ["pitch_usage"])
    print(pitcher_most_used)

    team_df = team_dict[Config.opp_team]
    batter_dfs = []
    for pitch in pitcher_most_used["pitch_name"].values:
        print(pitch)
        team_pitch_match = team_df[team_df["pitch_name"] == pitch]
        team_highest_ba = team_pitch_match.nlargest(5, ["ba"])
        team_highest_ba = team_highest_ba.sort_values(by="ba", ascending=False)
        batter_dfs.append(team_highest_ba)
        print(team_highest_ba)

    save_data(pitcher_most_used, batter_dfs)
    return