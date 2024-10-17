#Q.no.1
class Car:
    current_speed = 0
    travelled_distance = 0
    def __init__(self, registration_number, maximum_speed ):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed




car1 = Car("ABC-123", "142 km/h")
print(f"The registration number of the car is {car1.registration_number}")
print(f"The maximum speed of the car is {car1.maximum_speed} ")


#Q.no.2
class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0

    def accelerate(self, speed_change):

        new_speed = self.speed + speed_change


        if new_speed > self.max_speed:
            self.speed = self.max_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def __str__(self):
        return f"Current speed: {self.speed} km/h"


my_car = Car(max_speed=150)


my_car.accelerate(30)
print(my_car)

my_car.accelerate(70)
print(my_car)

my_car.accelerate(50)
print(my_car)

my_car.accelerate(-200)
print(my_car)

#Q.no.3
class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0
        self.distance_travelled = 0

    def accelerate(self, speed_change):

        new_speed = self.speed + speed_change


        if new_speed > self.max_speed:
            self.speed = self.max_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def drive(self, hours):

        distance_increase = self.speed * hours
        self.distance_travelled += distance_increase

    def __str__(self):
        return f"Current speed: {self.speed} km/h, Distance travelled: {self.distance_travelled} km"

my_car = Car(max_speed=150)


my_car.accelerate(30)
print(my_car)

my_car.accelerate(70)
print(my_car)

my_car.accelerate(50)
print(my_car)


my_car.drive(1.5)
print(my_car)

my_car.accelerate(-200)
print(my_car)

#Q.no.4
import random


class Car:
    def __init__(self, registration, max_speed):
        self.registration = registration
        self.max_speed = max_speed
        self.speed = 0
        self.distance_travelled = 0

    def accelerate(self, speed_change):

        new_speed = self.speed + speed_change

        if new_speed > self.max_speed:
            self.speed = self.max_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def drive(self, hours):
        distance_increase = self.speed * hours
        self.distance_travelled += distance_increase

    def __str__(self):
        return f"{self.registration:8} | {self.max_speed:10} | {self.speed:5} | {self.distance_travelled:10.1f} km"


cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration = f"ABC-{i}"
    car = Car(registration, max_speed)
    cars.append(car)

race_ongoing = True
hours_passed = 0

while race_ongoing:
    hours_passed += 1
    print(f"--- Hour {hours_passed} ---")

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

        if car.distance_travelled >= 10000:
            race_ongoing = False

print("\nRace finished! Final standings:")
print("Registration | Max Speed | Speed | Distance Travelled")
print("-------------|-----------|-------|--------------------")
for car in cars:
    print(car)