import math #for the calculation 
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
                continue
            else:
                return float(mass_value) #converting string to float
    def get_power(): #function to get input for engine power
        while True:
            power_value = input('Engine Power (kW): ')

            if not re.fullmatch(r"^\d{5,7}$", power_value): #only accepts number between 5 and 7 digits long
                print('Must be a realistic value...')
                continue
            else:
                return float(power_value) #converting string to float
            

    def get_drag():
    def get_area():
    def get_efficiency():
    def menu(): #display menu for user to chose what action to take
        car = Car(1600,120000,0.25,2.2,0.85) #estimated averages in place already if any info is missing calculations can still be done

        while True:
            print('\n(1) Calculate 0-60mph\n(2) Change mass\n(3) Change engine power\n(4) Change drag coefficient\n(5) Change frontal area\n(6) Change drivetrain efficiency\n(7) Save car\n(8) Load car\n(9) Exit')
            choice = input('Choose an option: ')

            if not choice.isdigit(): #make sure input is a number
                continue
            
            choice = int(choice) #converting string to integer

            if choice == 1: 
                time = calculate_time(Car) 
                print(f'0-60mph in: {time} seconds') 
            elif choice == 2:
                Car.mass = get_mass()
                print(f'Mass changed to {Car.mass}')
            elif choice ==3:
                Car.power = get_power()
            elif choice == 4:
                Car.drag = get_drag()
            elif choice == 5:
                Car.area = get_area()
            elif choice == 6:
                Car.efficiency = get_efficiency()
    menu()



        
