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
    
    class Car: #setting class for values to be input
        def __init__(self,mass,power,drag,area,efficiency):
            self.mass = mass
            self.power = power
            self.drag = drag
            self.area = area
            self.efficiency = efficiency

    def calculate_time(Car): #this function will do the calculation
        velocity = 0.00000001 #negligable start velocity to not divide by 0
        time = 0

        
