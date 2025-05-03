# Course CIS261 Week 4.2 Lab: Country guide
# Emma Kailani Tirado 05/02/2025
# The Country Guide Programm

# view
def country_guide():
    print("\nThe Country List Program")
    print("\nCOMMAND MENU")
    print("view - View a country")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program\n")

# Enter country code:
def view_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        print(F"Country name: {countries[code]}")
    else:
        print("Country code not found.")

# add
def add_country(countries):
    code = input("Enter country code: ").upper()
    name = input("Enter country name: ")
    countries[code] = name
    print(f"{name} was deleted.")

# del
def del_country(countries):
    code = input("Enter country code: ").upper()
    if code in countries:
        name = countries.pop(code)
        print(F"{name} was deleted.")
    else:
        print("Country code not found.")

def main():
    countries = {
        "US": "United States",
        "CA": "Canada",
        "MX": "Mexico"
    }

    country_guide()

    while True:
        command = input("\nCommand: ").lower()
        if command == "view":
            view_country(countries)
        elif command == "add":
            add_country(countries)
        elif command == "del":
            del_country(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again. ")

if __name__ == "__main__":
    main()