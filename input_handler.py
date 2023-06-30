from config import Config
import pandas as pd

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
    while(Config.pitcher == None):
        pitcher_id = input("Input Pitcher Player ID, use database if necessary: ")
        if validate_pitcher(pitcher_id) == True: Config.pitcher = int(pitcher_id)
    
    while(Config.opp_team == None):
        team_id = input("Input Opposing Team Abbreviation: ")
        if validate_team(team_id): Config.opp_team = team_id

    return