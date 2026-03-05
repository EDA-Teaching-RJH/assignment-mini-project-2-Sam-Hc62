import re #for accepting correct inputs
import json #for saving and loading
def main():
    #defining constants
    air_density = 1.225   
    gravity = 9.81
    rolling_resistance_coefficient = 0.015
    target_speed = 26.8  # 26m/s = 60mph
    time_step = 0.01 
    
    class Car: #setting up class for values to be input
        def __init__(self,mass,power,drag,area,efficiency):
            self.mass = mass
            self.power = power
            self.drag = drag
            self.area = area
            self.efficiency = efficiency

    def calculate_time(Car): #this function will do the calculation
        velocity = 0.00000001 #negligable start velocity to not divide by 0
        time = 0
        while velocity < target_speed: #count until 60mph is reached
            engine_force = (Car.power*Car.efficiency)/velocity 
            drag_force = 0.5*air_density*Car.drag*Car.area*velocity**2
            rolling_force = rolling_resistance_coefficient*Car.mass*gravity
            net_force = engine_force-drag_force-rolling_force
            acceleration = net_force/Car.mass
            velocity += acceleration*time_step
            time += time_step #counting in increments of 0.01
        return round(time, 2) #rounding final value to 2dp


    def get_mass(): #function to get input for mass
        while True:
            mass_value = input('Mass (Kg): ')

            if not re.fullmatch(r"^\d{3,4}$", mass_value): #only allows 3-4 digits
                print("Must be a realistic value...")
                continue #asks for input again
            else:
                return float(mass_value) #converting string to float and returning the value to the menu and then class
            
    def get_power(): #function to get input for engine power
        while True:
            power_value = input('Engine Power (kW): ')

            if not re.fullmatch(r"^\d{5,7}$", power_value): #only accepts number between 5 and 7 digits long
                print('Must be a realistic value...')
                continue #asks for input again
            else:
                return float(power_value) #converting string to float and returning the value to the menu and then class
            
    def get_drag(): #function to get drag input
        while True:
            drag_value = input('Drag Coefficient')

            if not re.fullmatch(r"^0\.\d{2}$", drag_value): #only accepting 0.XY format
                print('Must be a realistic value...')
                continue #asks for input again
            else:
                return float(drag_value) #converting string to float and returning the value to the menu and then class
            
    def get_area(): #function to get area input
        while True:
            area_value = input('Frontal Area (m²): ')

            if not re.fullmatch(r"^(?:1\.[5-9]\d*|[23](\.\d+)?)$", area_value): #only accepting numbers between 1.5 and 4
                print('Must be a realistic value...')
                continue #asks for input again
            else:
                return float(area_value) #converting string to float and returning the value to the menu and then class
            
    def get_efficiency(): #function to get efficiency input
        while True:
            efficiency_value = input('Drivetrain Efficiency: ')

            if not re.fullmatch(r"^0\.\d{2}$", efficiency_value): #only accepting 0.XY format
                print('Must be a realistic value...')
                continue #asks for input again
            else:
                return float(efficiency_value) #converting string to float and returning the value to the menu and then class

    def save_to_file(Car): #function to save current values to a json file
        with open("car_data.json", "w") as f: #opens file in write mode, if it doesn't exist it will be created
            json.dump(Car.__dict__, f) #saves the attributes of the Car class as a dictionary to the json file
        print("Car data saved.")   

    def load_car():#function to load values from json file
        try:
            with open("car_data.json", "r") as f: #opens file in read mode
                car_file = json.load(f) #loads the data from the json file and stores it in a variable
            print("Car data loaded.") 
            return Car(**car_file) #creates a new Car object using the data loaded from the json file
        except FileNotFoundError:
            print("No saved file found.")
            return None
          
    def display_values(cls, Car): #function to displays current values in a table format
        print(f"{'Mass':<10}{'Engine Power':<15}{'Drag Coefficient':<20}{'Frontal Area':<15}{'efficiency':<11}")
        print("-"*71)
        for s in Car:
            print(f"{s.mass:<10}{s.power:<15}{s.drag:<20}{s.area:<15}{s.efficiency:<11}")

    def menu(): #display menu for user to chose what action to take
        car = Car(1600,120000,0.25,2.2,0.85) #estimated averages in place already if any info is missing calculations can still be done

        while True:
            #printing menu options for user
            print('\n(1) Calculate 0-60mph\n(2) Change mass\n(3) Change engine power\n(4) Change drag coefficient\n(5) Change frontal area\n(6) Change drivetrain efficiency\n(7) Save car\n(8) Load car\n(9) Display values\n (10) Exit')
            choice = input('Choose an option: ') #getting user input for menu choice

            if not choice.isdigit(): #make sure input is a number
                continue
            
            choice = int(choice) #converting string to integer

            if choice == 1: 
                time = calculate_time(Car) #opens the calculation function 
                print(f'0-60mph in: {time} seconds')  #prints the result of the calculation
            elif choice == 2:
                Car.mass = get_mass() #opens the function to get mass input and changes the value in the class
                print(f'Mass changed to {Car.mass}') #prints the new value of mass
            elif choice ==3:
                Car.power = get_power() #opens the function to get engine power input and changes the value in the class
                print(f'Engine power changed to {Car.power}') #prints the new value of engine power
            elif choice == 4:
                Car.drag = get_drag() #opens the function to get drag coefficient input and changes the value in the class
                print(f'Drag coefficient changed to {Car.drag}') #prints the new value of drag coefficient
            elif choice == 5:
                Car.area = get_area() #opens the function to get frontal area input and changes the value in the class
                print(f'Frontal area changed to {Car.area}') #prints the new value of frontal area
            elif choice == 6:
                Car.efficiency = get_efficiency() #opens the function to get drivetrain efficiency input and changes the value in the class
                print(f'Drivetrain efficiency changed to {Car.efficiency}') #prints the new value of drivetrain efficiency
            elif choice == 7:
                save_to_file(Car) #opens the function to save the values to a json file
            elif choice == 8:
                loaded_car = load_car() #opens the function to load values from a json file
                if loaded_car:
                    Car = loaded_car #if a car was successfully loaded, it replaces the current Car object with the loaded one
            elif choice == 9:
                display_values(Car)
    menu()