#Justin King
#10/20/2024
#P3LAB
#money calculating program

#makes the float to an integer and calculates the number of each coin
def calculate_coins(amount):
    cents = int(amount * 100)
    dollars = cents // 100  
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5  
    pennies = cents % 5
    # store the results
    result = {}  
    # adds non-zero coin counts to the results
    if dollars > 0:
        result['Dollar' if dollars == 1 else 'Dollars'] = dollars  
    if quarters > 0:
        result['Quarter' if quarters == 1 else 'Quarters'] = quarters  
    if dimes > 0:
        result['Dime' if dimes == 1 else 'Dimes'] = dimes
    if nickels > 0:
        result['Nickel' if nickels == 1 else 'Nickels'] = nickels
    if pennies > 0:
        result['Penny' if pennies == 1 else 'Pennies'] = pennies
        return result

def main():
    while True:
        try:
            amount = float(input("Enter the amount of money as a float: $"))
            if amount < 0:
                print("Please enter a positive amount.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    coins = calculate_coins(amount)
    
    if not coins:
        print("No change")
    else:
        for coin, count in coins.items():
            print(f"{count} {coin}") 

if __name__ == "__main__": 
    main()
    

