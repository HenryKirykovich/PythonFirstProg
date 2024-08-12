#Assignment: Average Miles Per Gallon
#Class: DEV 108
#Date: 10/17/2023
#Author: Henadzi Kirykovch
#Description: Program to calculate the Average Miles Per Gallon

# Welcome message printed
print("Welcome to the Average MGP Calculator")
print()
while True:  # launching cycle of validation odometer
    start = int(input("Please enter the starting odometr reading in miles: "))  # Prompt the user for starting odometer reading
    if start < 0:
        print("Please put a valid mileage greater than zero")
        continue
    else:
        start >=0
        break
print()

# Initializing variables for save result and calculated MPG

leg_number = 0   # save amount leg
new_odo = 0      # save amount odometer
fuel = 0         # save amount fuel   
total_miles = 0  # total amount miles
total_fuel = 0   # total amount spent fuel 
choice = "y"     
while choice.lower() == "y":
    print("-"*100) 
    new_odo = int(input(f"Please enter new odometr reading in miles for leg # {leg_number+1}:  "))   # Prompt the user for new odometer reading and fuel consumed
    fuel = float(input(f"Please enter fuel consumed in gallon for leg # {leg_number+1}:  "))
    if (fuel > 0 and new_odo > start ):      # If fuel is positive and new odometer reading > last odometer reading:
        leg_number +=1
        MPG = round(((new_odo-start) / fuel), 1)  # Calculate MPG for this leg using mpg = (new odometer – last odometer) / fuel
        print("MPG for leg #", leg_number,  "=", MPG)
        
        total_miles += new_odo - start  # Accumulating the miles
        total_fuel +=fuel                # Accumulating fuel
        start = new_odo                  # changing odometer for the new cycle
        choice = input("Continue? (y/n): ")     # Ask if user wants to continue
    else:
        print( "Fuel consumed needs to positive and new odoment reading needs to be higher than", start)
        continue
print()
print("Total number of leg in the journey #",leg_number)  
print("Final average MPC for the enter journey: ", ( total_miles / total_fuel))  # Calculate average MPG over entire journey (= Total miles travelled / total fuel consumed)
print("Bye!")
            



 
    
    

    
    
