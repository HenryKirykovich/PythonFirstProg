
print("Welcome to the Prime Number Checker")
print()
# 
number = int(input("Please enter an integer between 1 and 5000: "))
while number >= 5000 or number <= 0:
    print ("Invalid integer.Please try again")
    number = int(input("Please enter an integer between 1 and 5000: "))
    
print ("Factor: ",end ="")
total_count = 0
for count in range(1, number+1):
    if number % count == 0:
        total_count +=1
        print(count, end=" ")
print("\nIt has ", total_count, "factors")
        

if (total_count == 2):
    print (f"{number} is a prime number")
else:
    print (f"{number} is NOT a prime number")
print()
print("Bye!")
   

# print("Welcome to the Funnyvile Packing Company")
# print("-"*50) 
# choice = "y"
# rate = 0
# total_pay = 0
# while choice.lower() == "y":
    # number = int(input("Enetr number of packages on a day: "))
    # if number < 0:
        # print("please enter valid positive number")
        # continue
    # 
    # if 1 <= number <= 49:
        # rate = 2.0
    # elif 50 <= number <= 100:
        # rate = 4.5
    # elif number  == 0:
        # rate = 0    
    # else:
        # number > 100
        # rate = 8.5
    # 
    # pay_day = number * rate
    # total_pay += pay_day
    # 
    # print(f"Payment for that day:{pay_day}")
    # print(f"Payment for that day: {total_pay}")
    # choice = input("Continue (y/n)")
    # 
# print("-"*50)
# print("Total Payment so for:", total_pay)
# print("Bye!")

           

    

