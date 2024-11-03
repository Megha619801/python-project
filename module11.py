#Q.no.1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        raise NotImplementedError("Subclass should implement this method.")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book name : {self.name}")
        print(f"author : {self.author}")
        print(f"page_count : {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name : {self.name}")
        print(f"Chief_editor : {self.chief_editor}")

if __name__ == "__main__":
    magazine = Magazine("Donald Duck", "Aki Hyppa")
    book = Book("compartment no.6", "Rosa Liksom", 192)

    print("Magazine information: ")
    magazine.print_information()
    print("\nBook Information: ")
    book.print_information()

#Q.no.2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.kilometer_counter = 0

    def set_speed(self, speed):
        if speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.kilometer_counter += distance

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kilowatt-hours

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters

if __name__ == "__main__":
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.set_speed(150)
    gasoline_car.set_speed(120)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print(f"Electric Car (Registration: {electric_car.registration_number})")
    print(f"Kilometers driven: {electric_car.kilometer_counter} km")
    print(f"Gasoline Car (Registration: {gasoline_car.registration_number})")
    print(f"Kilometers driven: {gasoline_car.kilometer_counter} km")