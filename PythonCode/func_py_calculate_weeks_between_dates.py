# func_py_calculate_weeks_between_dates.py
from datetime import datetime

def func_py_calculate_weeks_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days // 7

date1 = datetime(2023, 1, 1)
date2 = datetime(2024, 1, 1)
print(func_py_calculate_weeks_between_dates(date1, date2))
