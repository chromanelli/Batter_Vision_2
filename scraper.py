import pybaseball as pyb
from config import Config

def get_batter_data(year, minPA):
    return pyb.statcast_batter_pitch_arsenal(year, minPA)

def get_pitcher_data(year, minPA):
    return pyb.statcast_pitcher_arsenal_stats(year, minPA)