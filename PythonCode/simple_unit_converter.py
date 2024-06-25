# simple_unit_converter.py
def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

if __name__ == "__main__":
    choice = input("Convert inches to cm or cm to inches? (i/c): ").strip().lower()
    if choice == 'i':
        inches = float(input("Enter inches: "))
        print(f"{inches} inches is {inches_to_cm(inches)} cm")
    elif choice == 'c':
        cm = float(input("Enter cm: "))
        print(f"{cm} cm is {cm_to_inches(cm)} inches")
    else:
        print("Invalid choice")
