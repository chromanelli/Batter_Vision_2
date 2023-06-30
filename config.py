from enum import Enum
from datetime import date

class Config(Enum):
    year = 2023
    minPA = 25
    start_date = "2023-03-30"
    end_date = date.today()
    batters = ["rafael_devers"]