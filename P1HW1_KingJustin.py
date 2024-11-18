#Justin King
#09/29/2024
#P1HW1
#creating a program that will calculate exponents and do addition and subtraction
print("-----Calculating Exponents-----")
base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent_value
print(f"{base_value} raised to the power of {exponent_value} is {result}")

print("-----Addition and Subtraction-----")
base_value2 = int(input("Enter a starting integer: "))
exponent_value2 = int(input("Enter an integer to add: "))
exponent_value3 = int(input("Enter an integer to subtract: "))
result = base_value2 + exponent_value2 - exponent_value3
print(f"{base_value2} + {exponent_value2} - {exponent_value3} = {result}")     
