#Assignment: Rock-Paper-Scissors Game
#Class: DEV 108
#Date: 11/10/2023
#Author: Henadzi Kirykovch
#Description: It is the popular game Rock-Paper-Scissors

# Welcoming: Print the welcome message and Print the rules of the game.

import random
#Function to print the welcome message and the rules of the game
def printWelcome():      
    print ("Welcome to Rock/Paper/Scissors game")
    rules = """
    Rules of the game:
        Scissors wins over Paper (it can cut the paper) but loses to Rock (it can get crushed by the rock)
        Paper wins over Rock (it can wrap the rock) but loses to Scissors (it can be cut by scissors)
        Rock wins over Scissors( it can crush the scissors) but loses to Paper (it can be wrapped by paper)
    You repeat the rounds until user picks “(q)uit” to quit the game.
    """    
    print(rules)
#Function to prompt the user for the pick (including quit).
def getUserPick():
    print("Let the game begin!! Entere 'q' to quit.")
    print()
    user_choice = input("Your turn. Pick (r)ock, (p)aper, (s)cissors: ").lower()
    return user_choice
 #  Function that compares the user and computer choice and returns who the winner is (“tie”, “user” or “computer”). 
def pickRPS(): 
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp = "rock"
    elif comp_choice == 2:
        comp = "paper"
    elif comp_choice == 3:
        comp = "scissors"
    return comp
#Function that simulates the computer picking its choice
def getResult(user,comp):
    if (user == "r" and comp =="rock") or (user == "p" and comp =="paper") or (user == "s" and comp =="scissors"):
        getResult = "Its a tie"
    elif (user == "r" and comp == "scissors") or (user == "p" and comp == "rock") or (user == "s" and comp == "paper"):
        getResult = "User wins"
    elif (user == "r" and comp == "paper") or (user == "p" and comp == "scissors") or (user == "s" and comp == "rock"):
        getResult = "Computer wins"
    return getResult
# The main function that ties all these functions together
def main():
    printWelcome()
    countUserWins = 0
    countComputerWins = 0
    countTies = 0
    countTotal = 0
    print() 
    user = getUserPick()
    while user.lower() != "q":
        comp = pickRPS()
        print()
        print("You picked", user, "Computer picked", comp)
        result = getResult(user,comp)
        print(result)
        user = getUserPick()
        countTotal +=1
        if result ==  "Its a tie":
            countTies +=1
        elif result == "User wins":
            countUserWins +=1
        elif result == "Computer wins":
            countComputerWins +=1
    
    #Print final counts
    print("Number of round:", countTotal)
    print("Number of times you won", countUserWins)
    print("Number of times Computer won", countComputerWins)
    print("Number of ties :", countTies)    
    print()
    print("Bye!")
if __name__ == "__main__":
    main()