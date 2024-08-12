#Assignment: Net pay calculator 
#Class: DEV 108
#Date: 9/23/2023
#Author: Henadzi Kirykovch
#Description: Program to calculate the net pay given hours worked, hourly rate and tax withholding percent

#introducig programm 
print("Welcome to Net Pay Calculator")
print()
#declaring variables and put information on there
name = str(input("Your name: "))
h_work = int(input("Hours Worked: "))
h_pay_rate = int(input("Hourly pay rate: "))
tax_with_per = float(input("Tax withholding percentage %: "))
print()
# calculating gross pay,tax,net pay
gross_pay = h_work * h_pay_rate
tax = gross_pay * tax_with_per / 100
net_pay = round(gross_pay - tax, 2)

# viewing the result
print("Hello " + name + "!")
print("Your Gross Pay: $" + str(gross_pay))
print("Your Net Pay: $" + str(net_pay))
print("Good bye!")
