#!/usr/bin/env python3
# Created by Maximiliano Fairman
# Created on Nov 12th, 2025
# this program ask the user to enter a whole number.
# It then uses a do..while loop to calculate the factorial
# of that number.


# Factorial calculator with simplified comments

def main():
    # Get user input as text
    input2_value = input("Enter a positive whole number: ")

    try:
        # Convert input to integer
        user_number = int(input2_value)

        # Repeat until the user enters a non-negative number
        while user_number < 0:
            print("That is not a positive whole number. Try again.\n")
            input2_value = input("Enter a positive whole number: ")
            user_number = int(input2_value)

        # Calculate factorial
        factorial = 1
        counter = 1

        while True and counter <= user_number:
            factorial *= counter
            counter += 1

        # Display results
        print(f"{counter = }, {factorial = }")
        print(f"The factorial of {user_number} is {factorial}.")

    except ValueError:
        # If conversion fails
        print(f"Please enter a WHOLE NUMBER, not '{input2_value}'.")


if __name__ == "__main__":
    main()
# End of program

