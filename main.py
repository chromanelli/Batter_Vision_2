from config import Config
import scraper as scrpr
import os
from calculations import calculate

if __name__ == "__main__":
    if not os.path.exists("data/batter_data.csv"):
        batter_data = scrpr.get_batter_data(Config.year.value, Config.minPA.value)
        batter_data = batter_data.sort_values("player_id")
        batter_data.to_csv("data/batter_data.csv")

    if not os.path.exists("data/pitcher_data.csv"):
        pitcher_data = scrpr.get_pitcher_data(Config.year.value, Config.minPA.value)
        pitcher_data = pitcher_data.sort_values("player_id")
        pitcher_data.to_csv("data/pitcher_data.csv")

    calculate()