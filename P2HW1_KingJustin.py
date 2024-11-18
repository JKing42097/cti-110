#Justin King
#10/13/2024
#P2HW1
#a program for calculating travel expenses
print("-----Travel cost calculator-----")
#Enter in the variable values
budget_value = int(input("Enter your travel budget: "))
destination_value = input("Enter your destination: ")
gas_value = int(input("Enter Gas costs: "))
accommodation_value = int(input("Enter accommodation costs: "))
food_value = int(input("Enter food costs:  "))
#Set up formula to calculate the budget
result = budget_value - (gas_value + accommodation_value + food_value )
print("-----Travel Expenses-----")
#display results
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20} {destination_value}")
print(f"{'Initial Budget:':<20} ${budget_value:.2f}")
print(f"{'Fuel:':<20} ${gas_value:.2f}")
print(f"{'Accommodation:':<20} ${accommodation_value:.2f}")
print(f"{'Food:':<20} ${food_value:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<20} ${result:.2f}")
