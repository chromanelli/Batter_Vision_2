import pybaseball as pyb
from config import Config

def get_batter_data(p_name):
    search_name = p_name.split("_")
    batter = pyb.playerid_lookup(search_name[1], search_name[0])
    print(batter)
    b_id = batter['key_mlbam'].values[0]

    print("Searching: {:} ({:})".format(p_name, b_id))

    batter_data = pyb.statcast_batter(Config.start_date.value, Config.end_date.value, b_id)
    batter_data = batter_data[["game_date", "batter", "pitcher", "events", "description",
    "zone", "des", "balls", "strikes", "outs_when_up", "pitch_number", "inning", "plate_x", "plate_z"]]
    return batter_data