from datetime import date, timedelta

class Config():
    year = 2023
    minPA = 25

    # Change these as needed
    start_date = date.today() - timedelta(days=1) # Either 1 or 2
    end_date = date.today() # - timedelta(days=1)
    
    pitcher = None
    opp_team = None

    dirName = None
    batter_files = []