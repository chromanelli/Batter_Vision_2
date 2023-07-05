import pandas as pd
import scraper as scrpr
from config import Config

def make_statcast():
    pitcher_statcast = scrpr.get_game_data()
    pitcher_best = pd.read_csv(Config.dirName + "/pitcher_best.csv")
    best_pitches_type = pitcher_best["pitch_type"].values
    best_pitches_name = pitcher_best["pitch_name"].values
    
    pitcher_statcast = pitcher_statcast.loc[
        (pitcher_statcast["pitch_type"].isin(best_pitches_type)) |
        (pitcher_statcast["pitch_name"].isin(best_pitches_name))]

    hit_events = ["single", "double", "triple", "home_run"]
    pitcher_statcast = pitcher_statcast.loc[
        pitcher_statcast["events"].isin(hit_events)]

    pitcher_statcast.to_csv(Config.dirName + "/statcast.csv")
    print(pitcher_statcast)
    return pitcher_statcast

def analyze():
    statcast_df = make_statcast()
    batter_hits = statcast_df["batter"].unique()
    prediction = False
    for file in Config.batter_files:
        batter_df = pd.read_csv(file)
        predicted_batters = batter_df["player_id"].values
        for batter in batter_hits:
            if batter in predicted_batters:
                print(str(batter) + " was predicted")
                prediction = True

    if prediction == False:
        print("None found")

    return