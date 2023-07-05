import pybaseball as pyb
from config import Config
import pandas as pd

def get_batter_data(year, minPA):
    return pyb.statcast_batter_pitch_arsenal(year, minPA)

def get_pitcher_data(year, minPA):
    return pyb.statcast_pitcher_arsenal_stats(year, minPA)

def get_game_data():
    df = pd.read_csv(Config.dirName + "/pitcher_best.csv")
    pitcher_id = df["player_id"].values[0]
    return pyb.statcast_pitcher(str(Config.start_date), str(Config.end_date), pitcher_id)