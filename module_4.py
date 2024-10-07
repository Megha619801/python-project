#Q.no.1
i = 1

while i < 1000:
    if i%3==0:
        print(i)
    i+=1


#Q.no.2
while True:
    inches = float(input('enter the inches: '))
    if inches <0:
        print('program ends')
        break

    centimeter = inches * 2.54
    print(inches, 'inches is equal to ', centimeter, 'centimeters')


#Q.no.3

def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("That's not a valid number. Please try again.")

    if numbers:
        print(f"The smallest number is: {min(numbers)}")
        print(f"The largest number is: {max(numbers)}")
    else:
        print("No numbers were entered.")

find_min_max()

#Q.no.4


import random

def guess_the_number():

    number_to_guess = random.randint(1, 10)

    print("I'm thinking of a number between 1 and 10.")

    while True:

        guess = input("Take a guess: ")

        try:
            guess = int(guess)


            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Correct! You guessed the number!")
                break

        except ValueError:
            print("Please enter a valid number.")

guess_the_number()

#Q.no.5

def login():
    correct_username = "python"
    correct_password = "rules"


    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:

        username = input("Enter username: ")
        password = input("Enter password: ")


        if username == correct_username and password == correct_password:
            print("Welcome!")
            return


        attempts += 1
        print(f"Incorrect username or password. {max_attempts - attempts} attempts left.")


    print("Access denied.")

login()

#Q.no.6

import random


def calculate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)


        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1


    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation



num_points = int(input("Enter the number of random points to generate: "))


pi_value = calculate_pi(num_points)
print(f"The approximation of pi using {num_points} points is: {pi_value}")
