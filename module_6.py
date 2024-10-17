
#Q.no.2

import random
def roll_dice(times):
    return random.randint(1, times)

def main():
    times = int(input("Enter the number of sides on the dice: "))

    roll = 0
    while roll != times:
        roll = roll_dice(times)
        print(f"Rolled: {roll}")

main()

#Q.no.1
import random
def dice_roll():
    return random.randint(1, 6)

def main():
    roll = 0
    while roll != 6:
        roll = dice_roll()
        print(f"Rolled: {roll}")
main()

#Q.no.3
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


def main():
    while True:
        gallons = float(input("Enter the volume in gallons (negative value to quit): "))

        if gallons < 0:
            print("Exiting the program.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.\n")


main()

#Q.no.4
def sum_of_list(numbers):
    return sum(numbers)


def main():
    test_list = [10, 20, 30, 40, 50]

    result = sum_of_list(test_list)

    print(f"The sum of the list {test_list} is: {result}")


main()

#Q.no.5
def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    filtered_list = remove_odd_numbers(original_list)

    print(f"Original list: {original_list}")
    print(f"Filtered list (only even numbers): {filtered_list}")


main()

#Q.no.6
import math


def pizza_unit_price(diameter_cm, price_euros):
    diameter_m = diameter_cm / 100

    radius_m = diameter_m / 2
    area_m2 = math.pi * (radius_m ** 2)

    unit_price = price_euros / area_m2
    return unit_price


def main():
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"\nThe unit price of the first pizza is {unit_price1:.2f} euros per square meter.")
    print(f"The unit price of the second pizza is {unit_price2:.2f} euros per square meter.")

    if unit_price1 < unit_price2:
        print("\nThe first pizza offers better value for money.")
    elif unit_price1 > unit_price2:
        print("\nThe second pizza offers better value for money.")
    else:
        print("\nBoth pizzas offer the same value for money.")


main()

