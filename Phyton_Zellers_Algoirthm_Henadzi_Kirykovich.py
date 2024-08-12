#Assignment:  Zellers algorithm
#Class: DEV 108
#Date: 9/23/2023
#Author: Henadzi Kirykovch
#Description: Program to display day of the week for a given date

print( "Welcome to calculatare of day of week")

# 1. inizialisazing variables 
month = int(input("Enter month: "))
date = int(input("Enter the date: "))
years = int(input("Enter the year: "))
# 2. Validating of years such as the leap_years or simple years for next step  
if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
    leap = True
else:
    leap = False
# 3. Validates that all the input values are within bounds   
if (month == 2 and date > 29) or (month == 2 and date == 29 and leap ==False):
    print("invalid input, check day / leap / not leap year")
    quit()
elif ((month == 9 or month == 11 or month == 3 or month == 6) and date > 30):
    print("invalid input")
    quit()
elif ( 1 < month > 12 or 1 < date > 31 or 1582 < years > 4902):
    print("invalid input")
    quit()
# 4. Adjust month and year: Convert the entered month 
else:
    if month in [1, 2]:
        month_number = month + 10
        years_num = years - 1
    else:
        month_number = month - 2
        years_num = years
# 5. Calculate intermediate values:    
a = month_number
b = date
c = years_num % 100
d = years_num // 100
print ('a b c d =', a, b, c, d)
# 6.  Compute final values: 
w = int((13*a-1)/5)
x = int(c / 4)
y = int(d / 4)
z = int(w + x + y + b + c - 2*d)
r = int(z % 7)
print ("w x y z r = ", w, x, y, z, r)
# 7. Adjust r and print out day of the week:
if r < 0:
    r = r + 7
    if r == 0:
        date = "Sunday"
    elif r == 1:
        date ="Monday"
    elif r == 2:
        date = "Tuesday"
    elif r == 3:
        date = "Wednesday"
    elif r == 4:
        date = "Thursday"
    elif r == 5:
        date = "Friday"
    elif r == 6:
        date = "Saturday"
else:
    if r == 0:
        date = "Sunday"
    elif r == 1:
        date ="Monday"
    elif r == 2:
        date = "Tuesday"
    elif r == 3:
        date = "Wednesday"
    elif r == 4:
        date = "Thursday"
    elif r == 5:
        date = "Friday"
    elif r == 6:
        date = "Saturday"
print( "Day of the week: ", date)
print( "Bye!") 






