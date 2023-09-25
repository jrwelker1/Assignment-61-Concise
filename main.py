# Defines a parent class and stores the make and model for all vehicles.
class Vehicle:

    def __init__(self, make, model):
        # Initializes the make and model for all vehicles.
        self.make = make
        self.model = model
    
# DeFines a child class Car for parent class Vehicle.
class Car(Vehicle):

    def __init__(self, make, model, doors):
        # Uses the parent class Vehicle to set the make and model attributes.
        super().__init__(make, model)
        # Initializes number of doors attribute for cars.
        self.doors = doors
  
    def displayOption(self):
        # Displays the information for cars: make, model, and number of doors.
        print()
        print(f"The make is: {self.make}")
        print(f"The model is: {self.model}")
        print(f"The number of doors is: {self.doors}")

# Defines another child class Truck for parent class Vehicle.
class Truck(Vehicle):

    def __init__(self, make, model, bed_length):
        # Uses the parent class Vehicle to set the make and model attributes.
        super().__init__(make, model)
        # Initializes bed length attribute for trucks.
        self.bed_length = bed_length

    def displayOption(self):
        # Displays the information for trucks: make, model, and bed length.
        print()
        print(f"The make is: {self.make}")
        print(f"The model is: {self.model}")
        print(f"The bed length is: {self.bed_length}")

# Creates a loop for the user to select options.
while True:

    # Prompt for user input.
    selection = input("Enter 1 for car, 2 for truck, or 3 to quit: ")
    print()

    if selection == '1':
        make = input("Please enter make: ")
        model = input("Please enter model: ")
        doors = input("Please enter number of doors: ")
        # Creates a new car object and displays its information.
        new_car = Car(make, model, doors)
        print("\nCar added to garage.\n")

    elif selection == '2':
        make = input("Please enter make: ")
        model = input("Please enter model: ")
        bed_length = input("Please enter bed length: ")
        # Creates a new truck object and displays its information.
        new_truck = Truck(make, model, bed_length)
        print("\nTruck added to garage.\n")

    elif selection == '3':
        print("Thank you for using the program.")
        break

    else:
        print("Invalid entry, please enter 1, 2, or 3.\n")