#Assignment:  Rhyme
#Class: DEV 108
#Date: 11/02/2023
#Author: Henadzi Kirykovch
#Description: Program uses the functions to print the lyrics of a famous nursery rhyme

# 1. inizialisazing function printRefain
def printRefain():
    print("Old MacDonald had a farm\nEe i ee i o")
# 2. inizialisazing function printVerse that call another function printRefal
def printVerse(name_animal, sound_animal):
    printRefain()
    print(f"And on his farm he had some {name_animal}")
    print("Ee i ee i o")
    print(f"With a {sound_animal}-{sound_animal} here")
    print(f"And a {sound_animal}-{sound_animal} here")
    print(f"Here a {sound_animal}, there a {sound_animal}")
    print(f"Ewerywhere a {sound_animal}")
    printRefain()
    
# 3. Inizializing Main func. and input dates 
def main():
    choice = "y"
    while choice.lower() == "y":
        for n in range(1, 4):
            name_animal = input(f"Please input name of animal # {n}: ")
            sound_animal = input(f"Please input sound of animal # {n}: ")
            print()
            print( '"Old MacDonald"\n')
            print()
            printVerse(name_animal, sound_animal)
            print()
            print() 
        choice = input("Do you want to continue sing the song? (y/n) ")        
        print()
        print(f"Thank you, Bye! {sound_animal} ")         
        
             
if __name__ == "__main__":
    main()
    
    
     
