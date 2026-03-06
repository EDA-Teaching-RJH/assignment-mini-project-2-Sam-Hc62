import conversions #importing conversions file for converting values to the correct units
import re #for accepting correct inputs 
import json #for saving and loading
def main():
    name_pattern = re.compile(r"^[A-Za-z0-9 ]{1,20}$") #regex pattern to validate car names, allowing letters, numbers, and spaces, with a maximum length of 20 characters
    #defining constants
    air_density = 1.225   
    gravity = 9.81
    rolling_resistance_coefficient = 0.015
    target_speed = 26.8  # 26m/s = 60mph
    time_step = 0.01 
    
    class Vehicle: #base class for vehicles
        def __init__(self, mass):
            self.mass = mass


    class Car(Vehicle): #subclass for values
        def __init__(self, mass, power, drag, area, efficiency): 
            super().__init__(mass) #inheritance 
            self.power = power
            self.drag = drag
            self.area = area
            self.efficiency = efficiency

    def calculate_time(car): #this function will do the calculation
        velocity = 0.1 #small start velocity to not divide by 0
        time = 0
        while velocity < target_speed: #count until 60mph is reached
            engine_force = (car.power*car.efficiency)/velocity 
            drag_force = 0.5*air_density*car.drag*car.area*velocity**2
            rolling_force = rolling_resistance_coefficient*car.mass*gravity
            net_force = engine_force-drag_force-rolling_force
            acceleration = net_force/car.mass
            velocity += acceleration*time_step
            time += time_step #counting in increments of 0.01
        return round(time, 2) #rounding final value to 2dp

    def get_mass(): #function to get input for mass
        while True:
            mass_value = input('\nMass (Kg): ')

            if not re.fullmatch(r"^\d{3,4}$", mass_value): #only allows 3-4 digits
                print("Must be a 3-4 digit integer...") 
                continue #asks for input again
            else:
                return int(mass_value) #converting string to integer and returning the value to the menu and then class
            
    def get_power(): #function to get input for engine power
        while True:
            power_value = input('\nEngine Power (kW): ')

            if not re.fullmatch(r"^\d{2,4}$", power_value): #only accepts number between 2 and 4 digits long
                print('Must be a 2-4 digit integer...')
                continue #asks for input again
            else:
                return float(power_value)*1000 #converting string to float and returning the value to the menu and then class, x1000 to convert from kW to W
            
    def get_drag(): #function to get drag input
        while True:
            drag_value = input('\nDrag Coefficient (%): ')

            if not re.fullmatch(r"^\d{1,2}$", drag_value): #only accepting 1-2 digit numbers
                print('Must be a one or two digit integer...')
                continue #asks for input again
            else:
                return float(drag_value)/100 #converting string to float and returning the value to the menu and then class
            
    def get_area(): #function to get area input
        while True:
            area_value = input('\nFrontal Area (m²): ')

            if not re.fullmatch(r"^(?:1\.[5-9]\d*|[23](\.\d+)?)$", area_value): #only accepting numbers between 1.5 and 4
                if not area_value.isdigit():
                    print('Error...')
                    continue
                area_value = float(area_value) #converting string to float to check the value
                if area_value > 4:
                    print('Must be less than 4m²')
                    continue
                elif area_value < 1.5:
                    print('Must be greater than 1.5m²')
                    continue
            else:
                return float(area_value) #converting string to float and returning the value to the menu and then class
            
    def get_efficiency(): #function to get efficiency input
        while True:
            efficiency_value = input('\nDrivetrain Efficiency (%): ')

            if not re.fullmatch(r"^\d{2}$", efficiency_value): #only accepting 2 digit numbers
                print('Must be a two digit integer...')
                continue #asks for input again
            else:
                return float(efficiency_value)/100 #converting string to float and returning the value to the menu and then class

    def save_to_file(car): #function to save values to a json file
        try:
            with open("car_data.json", "r") as f: #try to open the file and load existing data  
                cars = json.load(f) 
        except (FileNotFoundError, json.JSONDecodeError): #if file does not exist or is empty, start with an empty list
            cars = []
        while True:
            name = input("Enter a name for this car: ").strip() #asking user for a name to save the car under, stripping whitespace from the input
            if not name_pattern.fullmatch(name):
                print("Name must be less than 20 characters...\n")
                continue #asks for input again    
            else:
                break
        cars.append({'name': name,'mass': int(car.mass),'power': int(car.power/1000),'drag': round(car.drag, 2),'area': car.area,'efficiency': car.efficiency}) #adding the new car to the list of cars 

        try:
            with open("car_data.json", "w") as f: #opening the file in write mode and saving the updated list of cars back to the file
                json.dump(cars, f, indent=2) 
            print(f"'{name}' saved...") 
        except Exception as e: #catching any exceptions that may occur during the file writing process 
            print(f"Error saving car: {e}")

    def load_car():
        try:
            with open("car_data.json", "r") as f: #try to open the file and load existing data
                cars = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError): #if file does not exist or is empty, returns nothing
            print("No saved cars found.")
            return None

        if not cars: #if file does not exist or is empty, returns nothing
            print("No saved cars found in the file.")
            return None

        print("\nSaved Cars:")
        print("-"*82)
        print(f"|{' No.':<4}{'| Name':<20}{'| Mass(Kg)':<11}{'| Power(kW)':<12}{'| Drag':<8}{'| Area(m²)':<11}| {'Efficiency'}  |")
        print("-"*82)
        for idx, c in enumerate(cars, 1):
            print(f"| {idx:<3}| {c['name']:<18}| {c['mass']:<9}| {c['power']:<10}| {c['drag']:<6}| {c['area']:<9}| {int(c['efficiency']*100)}%         |") #printing the list of saved cars in a table format with an index number for selection
        print("-"*82)

        while True:
            try:
                choice_2 = int(input("\nEnter the number of the car to load: "))
                if 1 <= choice_2 <= len(cars):
                    selected = cars[choice_2-1]
                    return Car(mass=selected['mass'],power=selected['power']*1000,drag=selected['drag'],area=selected['area'],efficiency=selected['efficiency'])
                else:
                    print("enter a valid number from the list...")
                    continue
            except ValueError:
                continue
            
    def display_values(car): #function to displays current values in a table format
        print("\nCurrent values:")
        print("-"*76)
        print(f"| {'Mass':<8}| {'Engine Power':<14}| {'Drag Coefficient':<18}| {'Frontal Area':<14}| {'Efficiency':<9} |")
        print("-"*76)
        print(f"{f'| {car.mass}Kg':<10}{f'| {conversions.W_to_kW(car.power)}kW':<16}{f'| {car.drag}':<20}{f'| {car.area}m²':<16}{f'| {conversions.decimal_to_percent(car.efficiency)}%':<13}|")
        print("-"*76)
    
    def menu(): #display menu for user to chose what action to take
        car = Car(1600,120000,0.25,2.2,0.85) #estimated averages in place already if any info is missing calculations can still be done

        while True:
            #printing menu options for user
            print('\n(1)  Calculate 0-60mph\n(2)  Change mass\n(3)  Change engine power\n(4)  Change drag coefficient\n(5)  Change frontal area\n(6)  Change drivetrain efficiency\n(7)  Save car\n(8)  Load car\n(9)  Display values\n(10) Exit')
            choice = input('\nChoose an option: ') #getting user input for menu choice

            if not choice.isdigit(): #make sure input is a number
                continue
            
            choice = int(choice) #converting string to integer

            if choice == 1: 
                time = calculate_time(car) #opens the calculation function 
                print(f'\n0-60mph in: {time}s')  #prints the result of the calculation
            elif choice == 2:
                car.mass = get_mass() #opens the function to get mass input and changes the value in the class
                print(f'Mass changed to {int(car.mass)}Kg') #prints the new value of mass
            elif choice ==3:
                car.power = get_power() #opens the function to get engine power input and changes the value in the class
                print(f'Engine power changed to {int(car.power/1000)}kW') #prints the new value of engine power
            elif choice == 4:
                car.drag = get_drag() #opens the function to get drag coefficient input and changes the value in the class
                print(f'Drag coefficient changed to {car.drag}') #prints the new value of drag coefficient
            elif choice == 5:
                car.area = get_area() #opens the function to get frontal area input and changes the value in the class
                print(f'Frontal area changed to {car.area}m²') #prints the new value of frontal area
            elif choice == 6:
                car.efficiency = get_efficiency() #opens the function to get drivetrain efficiency input and changes the value in the class
                print(f'Drivetrain efficiency changed to {car.efficiency*100}%') #prints the new value of drivetrain efficiency
            elif choice == 7:
                save_to_file(car) #opens the function to save the values to a json file
            elif choice == 8:
                loaded_car = load_car() #opens the function to load values from a json file
                if loaded_car:
                    car = loaded_car #if a car was successfully loaded, it replaces the current Car object with the loaded one
            elif choice == 9:
                display_values(car)
            elif choice == 10:
                print("Exiting program...")
                break #exits the loop and ends the program
            else:
                continue #if the user input does not match any of the options, it will ask for input again
    def run_tests():
        print("\nTesting program...")
        test_car = Car(1600,120000,0.25,2.2,0.85)
        result = calculate_time(test_car)
        if result > 0: #testing that the time is a positive value
            print("...3")
        else:
            print("Calculation test failed...")

        if conversions.W_to_kW(120000) == 120: #testing the watts to kW conversion
            print("...2")
        else:
            print("Power conversion test failed")

        if conversions.decimal_to_percent(0.85) == 85: #testing the efficiency percentage conversion 
            print("...1")
        else:
            print("Percentage conversion test failed")
        print("Testing complete...")
    run_tests()
    menu()
main()