#Q.no.1
seasons = ("winter", "winter", "spring", "spring", "spring",
           "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")


def main():
    month = int(input("Enter the number of the month (1-12): "))

    if 1 <= month <= 12:
        season = seasons[month - 1]
        print(f"The corresponding season is: {season}")
    else:
        print("Please enter a valid month number between 1 and 12.")


main()

#Q.no.2
def main():
    names = set()

    while True:
        name = input("Enter a name (or press Enter to stop): ")

        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nList of names entered:")
    for name in names:
        print(name)


main()

#Q.no.3
def main():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            icao_code = input("Enter the ICAO code of the airport: ").upper()
            name = input("Enter the name of the airport: ")

            airports[icao_code] = name
            print(f"Airport {name} with ICAO code {icao_code} added.")

        elif choice == "2":
            icao_code = input("Enter the ICAO code of the airport to fetch: ").upper()

            if icao_code in airports:
                print(f"The airport with ICAO code {icao_code} is {airports[icao_code]}.")
            else:
                print(f"No airport found with ICAO code {icao_code}.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please choose 1, 2, or 3.")


main()