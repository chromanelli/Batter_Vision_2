import pybaseball as pyb
from config import Config
import scraper as scrpr

def fix_name(player_name):
    f_name = player_name[0]
    l_name = player_name[1]
    ret = f_name[0].upper() + f_name[1:] + " " + l_name[0].upper() + l_name[1:]
    print(ret)
    return ret

if __name__ == "__main__":
    batters = Config.batters.value
    for p_name in batters:
        print(scrpr.get_batter_data(p_name))