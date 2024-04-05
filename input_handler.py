from config import Config
import pandas as pd
import os
import scraper as scrpr

def validate_pitcher(user_input):
    valid_pitchers = pd.read_csv("data/pitcher_data.csv")["player_id"].values
    if int(user_input) not in valid_pitchers:
        return False

    return True

def validate_team(user_input):
    valid_teams = pd.read_csv("data/batter_data.csv")["team_name_alt"].values
    if user_input not in valid_teams: return False
    
    return True

def get_input():
    update = None
    while(update == None):
        update = input("Update pitchers and batters? (y/n): ")
        if(update == 'y'):
            if not os.path.exists("data/"):
                os.mkdir("data")

            batter_data = scrpr.get_batter_data(Config.year, Config.minPA)
            batter_data = batter_data.sort_values("player_id")
            batter_data.to_csv("data/batter_data.csv")

            pitcher_data = scrpr.get_pitcher_data(Config.year, Config.minPA)
            pitcher_data = pitcher_data.sort_values("player_id")
            pitcher_data.to_csv("data/pitcher_data.csv")

        elif(update != 'n'):
            break
        else:
            update = None
        
    while(Config.pitcher == None):
        pitcher_id = input("Input Pitcher Player ID, use database if necessary: ")
        if validate_pitcher(pitcher_id) == True:
            Config.pitcher = int(pitcher_id)
    
    while(Config.opp_team == None):
        team_id = input("Input Opposing Team Abbreviation: ")
        if validate_team(team_id):
            Config.opp_team = team_id

    return