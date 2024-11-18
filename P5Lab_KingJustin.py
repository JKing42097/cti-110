#Justin King
#11/17/2024
#P5 Lab
#register program to calculate change per total

import random

def disperse_change(change_amount):
    # Convert to cents
    cents = round(change_amount * 100)

    # Calculate each denomination
    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    pennies = cents % 5

    # Display results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars != 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters != 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes != 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels != 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies != 1 else 'y'}")

def main():
    # Generate random amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    # Get payment 
    while True:
        try:
            payment = float(input("How much cash will you put in the self-checkout? "))
            if payment < amount_owed:
                print("Insufficient payment. Please enter an amount equal to or greater than what you owe.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate change
    change = round(payment - amount_owed, 2)
    print(f"Change is: ${change:.2f}")

    # Calculate and display coins
    disperse_change(change)

if __name__ == "__main__":
    main()
