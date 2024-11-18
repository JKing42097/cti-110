# Justin King
# 10/6/2024
# P2LAB2
#Car and MPG dictionary/calculator
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicles.keys()

print("Available vehicles:", list(keys))

vehicle = input("Enter a vehicle to see its MPG: ")

if vehicle in vehicles:
    mpg = vehicles[vehicle]
    print(f"The {vehicle} gets {mpg} mpg")

    miles = float(input("How many miles will you drive? "))

    gallons_needed = miles / mpg

    print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")
else:
    print("Vehicle not found in the list. Please check the spelling and try again.")
