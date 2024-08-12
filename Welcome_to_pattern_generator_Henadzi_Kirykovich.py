#Assignment: Welcome to pattern generator
#Class: DEV 108
#Date: 10/24/2023
#Author: Henadzi Kirykovch
#Description: In this assignment, you will write a program that creates patterns using for-loops given the size - an odd number between 7 and 15 (both inclusive).

#Display welcome message
print("Welcome to pattern generator")

#Validates that size is an odd number between 7 and 15 (both inclusive)
while True:
    odd_number = int(input("Please enter the size(ann odd number between 7 and 15): "))
    if (odd_number % 2 == 0) or 7 > odd_number or odd_number > 15:
        print("Size should be an odd number bettween 7 and 15.")
        continue
    else:
        break
# Print Pattern 1 
print("Pattern 1 of size", odd_number)
number = odd_number * 2+1
for i in range(1, odd_number+1):
    star = "*" * (number - i*2)
    print("("*i + star +")"*i)

# Print Pattern 2 separate picture on two parts + the one line "A" beetwen their    
print(f"Mirror image pattern of size {odd_number}") 
for i in range(1, odd_number):
    empty = " " * (odd_number*2 -i*2)
    print("A"*i + empty +"A"*i)
print("A"*odd_number*2) 
for i in range(1, odd_number):
    empty = " " * i*2
    numberA = odd_number-i
    print("A"*numberA + empty +"A"*numberA)
print()
print("Bye")

     


 
                  