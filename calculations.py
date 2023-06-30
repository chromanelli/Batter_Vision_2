import pandas as pd

def make_dicts():
    pitcher_df = pd.read_csv("data/pitcher_data.csv")
    batter_df = pd.read_csv("data/batter_data.csv")

    print(pitcher_df.columns)
    print(batter_df.columns)

    pitcher_ids = pitcher_df["player_id"].unique()
    pitcher_dict = {}
    for id in pitcher_ids:
        pitcher_dict[id] = pitcher_df[pitcher_df["player_id"] == id]
    
    batter_ids = batter_df["player_id"].unique()
    batter_dict = {}
    for id in batter_ids:
        batter_dict[id] = batter_df[batter_df["player_id"] == id]
    
    return pitcher_dict, batter_dict

def calculate():
    pitcher_dict, batter_dict = make_dicts()

    return