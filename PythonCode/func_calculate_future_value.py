# func_calculate_future_value.py
def func_calculate_future_value(principal, rate, time):
    return principal * (1 + rate)**time

print(func_calculate_future_value(1000, 0.05, 2))
