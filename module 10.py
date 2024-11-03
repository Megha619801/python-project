#Q.no.1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range!")
            return

        print(f"Moving to floor {target_floor}...")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Elevator has arrived at floor {self.current_floor}")



elevator = Elevator(bottom_floor=1, top_floor=10)

elevator.go_to_floor(5)

elevator.go_to_floor(1)

#Q.no.2
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range!")
            return

        print(f"Moving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        print(f"Building with {num_elevators} elevators created.")

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning Elevator {elevator_number + 1} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number + 1} does not exist in this building.")

    def __str__(self):
        return "\n".join(
            [f"Elevator {i + 1}: Current floor {elevator.current_floor}" for i, elevator in enumerate(self.elevators)]
        )


building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

building.run_elevator(0, 5)

building.run_elevator(1, 8)

building.run_elevator(2, 10)

print("\nCurrent status of all elevators:")
print(building)

#Q.no.3

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range!")
            return

        print(f"Moving to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        print(f"Building with {num_elevators} elevators created.")

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning Elevator {elevator_number + 1} to floor {destination_floor}")
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print(f"Elevator {elevator_number + 1} does not exist in this building.")

    def fire_alarm(self):
        print("\nFire alarm activated! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"\nMoving Elevator {i + 1} to the bottom floor:")
            elevator.go_to_floor(self.bottom_floor)

    def __str__(self):
        return "\n".join(
            [f"Elevator {i + 1}: Current floor {elevator.current_floor}" for i, elevator in enumerate(self.elevators)]
        )


building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

building.run_elevator(0, 5)

building.run_elevator(1, 8)

building.run_elevator(2, 10)

print("\nCurrent status of all elevators:")
print(building)

building.fire_alarm()

print("\nStatus of all elevators after fire alarm:")
print(building)

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
        self.distance_travelled += self.speed * hours

    def __str__(self):
        return f"{self.registration:8} | {self.max_speed:10} | {self.speed:5} | {self.distance_travelled:10.1f} km"


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':<12} | {'Max Speed':<10} | {'Speed':<5} | {'Distance Travelled':<10}")
        print("-" * 50)
        for car in self.cars:
            print(car)

    def race_finished(self):
        return any(car.distance_travelled >= self.distance for car in self.cars)


cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    registration = f"ABC-{i}"
    cars.append(Car(registration, max_speed))

race = Race(name="Grand Demolition Derby", distance=8000, cars=cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        race.print_status()

print("\n--- Race Finished ---")
race.print_status()