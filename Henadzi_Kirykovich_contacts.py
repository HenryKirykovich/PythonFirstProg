#Assignment: Contacts Manager 
#Class: DEV 108
#Date: 11/21/2023
#Author: Henadzi Kirykovch
#Description: It allows user to display all contact names, add a new contact or view, edit or delete an existing contact

# Contacts manager: a program that is used to manage the primary email
# address and phone number for a contact.

# function takes a list of names as argument.
def display(contacts_names):
    if (len(contacts_names) != 0):
        i = 1
        for item in contacts_names:
            print(str(i)+"." + item)
            i +=1
    else:
        print("There are no contacts in the list.") 

    
# prompts the user for data for a new contact and adds the information to the three lists. 
def add(names, emails, numbers):
    new_name = input("Name: ")
    names.append(new_name)
    new_emails = input("Email: ")
    emails.append(new_emails)
    new_numbers = input("Phone: ")
    numbers.append(new_numbers)
    print(new_name + " was added.")
    return add

# prompts the user for the contact number and prints the details of that contact as shown below. Checkin valid number in list
def view(names, emails, numbers):
    while True:
        number = int(input("Number: "))
        number_corr = (number - 1)
        if (number <= len(names)) and (number > 0):
            print("Name: " +names[number_corr])
            print("Email: " + emails[number_corr])
            print("Phone: " + numbers[number_corr])
            break
        elif ((number > len(names)) or (number <= 0)):
            print("Invalid contact number")
            break
            
           

#  prompts the user for the contact number and deletes the details of that contact from the three lists. Checkin valid number in list
def delete(names, emails, numbers):
    while True:
        number = int(input("Number: "))
        number_corr = number - 1
        if (number <= len(names)) and (number > 0):
            names_del = names[number_corr]
            names.pop(number_corr)
            emails.pop(number_corr)
            numbers.pop(number_corr)
        elif ((number > len(names)) or (number <= 0)):
            print("Invalid contact number")
            break
        print(names_del,"was deleted.")
        return delete  
# prompts the contact number of the contact whose phone number is to be edited; prompts new phone number and updates.Checkin valid number
def edit_phone(names, emails, numbers):
    while True:
        number = int(input("Number: "))
        number_corr = int(number - 1)
        if (number <= len(names)) and (number > 0):
            number_new = (input("New phone number: "))
            numbers[number_corr] = number_new
        elif ((number > len(names)) or (number <= 0)):
            print("Invalid contact number")
            break
        print(names[number_corr], "was edit")
        return edit_phone  
    
# it is title  
def show_title():
    print("Contact Manager")
    print()
#  it is menu before any process
def show_menu():
    print("COMMAND MENU")
    print("list - Show all contacts", end = "\t")
    print("view - View a contact")
    print("edit - Edit phone number",end = "\t")
    print("add  - Add a contact")
    print("del  - Delete a contact",end = " \t")
    print("exit - Exit program")
    print()    

def main():
    contacts_names = ["Harry Potter","Ron Weasley"]
    contacts_emails = ["hpotter@hogwarts.edu","rweasley@hogwarts.edu"]
    contacts_numbers = ["+44 20 6789 0022", "+44 20 2345 0958"]

    show_title()
    show_menu()
    # part of menu for choicing menu or off work   
    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts_names)
            print()
        elif command == "view":
            view(contacts_names, contacts_emails, contacts_numbers)
            print()
        elif command == "add":
            add(contacts_names, contacts_emails, contacts_numbers)
            print()
        elif command == "del":
            delete(contacts_names, contacts_emails, contacts_numbers)
            print()
        elif command == "edit":
            edit_phone(contacts_names, contacts_emails, contacts_numbers)
            print()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
