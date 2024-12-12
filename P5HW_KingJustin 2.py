#Justin King
#11/24/2024
#P5HW
#Math quiz program

import random

#generate numbers for math problem
def generate_numbers():
    """
    Generates two random numbers between 1 and 100
    Returns: tuple of two random integers
    """
    return random.randint(1, 100), random.randint(1, 100)

#sets quiz rules
def addition_game():
    """
    Implements the addition game logic:
    1. Generates two random numbers
    2. Asks user for the sum
    3. Provides feedback (too high/low)
    4. Tracks number of guesses
    5. Congratulates on correct answer
    """
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    
    print(f"{num1}")
    print(f"+ {num2}")
    
    guesses = 0
    while True:
        guesses += 1
        try:
            answer = int(input("\nEnter answer: "))
            if answer == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif answer < correct_answer:
                print("Sorry, guess is too low.")
                print("\nTry again:", end=" ")
            else:
                print("Sorry, guess is too high.")
                print("\nTry again:", end=" ")
        except ValueError:
            print("Please enter a valid number")
            guesses -= 1

def subtraction_game():
    """
    Implements the subtraction game logic:
    1. Generates two random numbers
    2. Asks user for the difference
    3. Provides feedback (too high/low)
    4. Tracks number of guesses
    5. Congratulates on correct answer
    """
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    
    print(f"{num1}")
    print(f"- {num2}")
    
    guesses = 0
    while True:
        guesses += 1
        try:
            answer = int(input("\nEnter answer: "))
            if answer == correct_answer:
                print("Congratulations!!!! Your answer is correct.")
                print(f"Number of guesses: {guesses}")
                break
            elif answer < correct_answer:
                print("Sorry, guess is too low.")
                print("\nTry again:", end=" ")
            else:
                print("Sorry, guess is too high.")
                print("\nTry again:", end=" ")
        except ValueError:
            print("Please enter a valid number")
            guesses -= 1

#Menu
def display_menu():
    """
    Displays the main menu with three options:
    1. Addition game
    2. Subtraction game
    3. Exit program
    """
    print("\nWelcome to Math Quiz")
    print("\nMAIN MENU")
    print("-" * 20)
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print("\nPlease choose one of the menu options:", end=" ")

#input control
def main():
    """
    Main program control flow:
    1. Displays menu
    2. Gets user choice
    3. Executes appropriate game or exits
    4. Handles invalid input
    5. Continues until user chooses to exit
    """
    while True:
        display_menu()
        choice = input()
        
        if choice == '1':
            addition_game()
        elif choice == '2':
            subtraction_game()
        elif choice == '3':
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Error: Invalid choice. Please enter 1, 2, or 3.")

# input
if __name__ == "__main__":
    main()
