#Justin King
#09/29/2024
#P1HW2
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
print(f"Location: {destination_value}")
print(f" Initial Budget: {budget_value}")
print(f"Fuel: {gas_value}")
print(f"Accommodation: {accommodation_value}")
print(f" Food: {food_value}")
print(f"Remaining balance: {result}")
