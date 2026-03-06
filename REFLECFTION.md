Regular expressions were used to check that user inputs were in the correct format. 
The re library was used in functions like get_mass(), get_power(), and get_drag() to make sure the user enters valid numbers. 
I also used a compiled regex pattern to check that car names only contain letters, numbers, and spaces and are under 20 characters long.

Basic testing was added through the run_tests() function. 
This runs a few checks when the program starts to make sure important parts of the program are working correctly
This was done for the acceleration calculation and the conversion functions.

The program uses the built-in re and json libraries. 
I also created a small custom module called conversions to handle unit conversions.

File handling is used so that car setups can be saved and loaded. 
The program stores the data in a car_data.json file and reads it back when needed.

Object-oriented programming is used by creating a Vehicle class and a Car class that inherits from it. 
The Car object stores properties like mass, power, drag, area, and efficiency, which are then used in the acceleration calculation. 