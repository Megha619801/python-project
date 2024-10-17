#Q.no.1
import random

num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0

for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print(f"The sum of your dice rolls is: {total_sum}")

#Q.no.2

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":
        break

    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

numbers.sort(reverse=True)

print("The five greatest numbers are:", numbers[:5])

#Q.no.3

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter an integer: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#Q.no.4

cities = []

for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

print("\nThe cities you entered are:")
for city in cities:
    print(city)
