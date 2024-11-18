#Justin King
#11/03/2024
#P4LAB2
#program for multiplication tables
while True:
    # Gather a number
    num = int(input("Enter an integer: "))

    # Check if number is negative
    if num < 0:
        print("This program does not handle negative numbers")
    else:
        #print multiplication table from 1 to 12
        for i in range(1, 13):
            print(f"{num} * {i} = {num * i}")

    # Ask if user wants to run again
    run_again = input("Would you like to run the program again? ")

    # Exit if user doesn't 
    if run_again.lower() != "yes":
        print("Exiting program...")
        break
