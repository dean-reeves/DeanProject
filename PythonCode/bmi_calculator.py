# bmi_calculator.py
def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = 70  # kg
height = 1.75  # meters
bmi = calculate_bmi(weight, height)
print(f"BMI is {bmi:.2f}")
