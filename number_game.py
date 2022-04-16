# Guess the Number Game!


import random

#Assigning a random integer to our random number variable
rand_number = random.randint(0, 100)

# Users will be able to input an integer continuously until they guess the hidden number correctly.
# This program will respond with whether the integer entered is higher, lower, or equal to the random integer.

while not False:

    # Setting hidden number to a variable
    hidden_number = rand_number
    guess_number = int(input("Guess the number :"))

    if(guess_number < hidden_number):
        print("Higher")
    elif(guess_number > hidden_number):
        print("Lower")
    else:
        print("Success")
        break