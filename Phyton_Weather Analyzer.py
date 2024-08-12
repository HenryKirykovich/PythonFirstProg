print("Welcome to Weather Analyzer")
print()
print()
unit = input("Please enter the units ('Enter F for Fahrenheit/ C for Celsius'):  ").lower
#if (unit.lower() == "F" or unit.lower() == "f" or unit.lower() == "C" or unit.lower() == "c"):
temp = float(input("Please enter the outside temperature: "))
    if unit == "F" or unit == "f":
        F = temp
        print("It is", temp, "degree outside")
        if F >80:
            print("It is too hot outside")
        elif F <60:
            print("It is chilly outside")
        else:
            print("It is very pleasent outside")
    elif unit == "C" or unit == "c":
        F = float(temp*1.8+32)
        print("It is", F, "degree outside")
        if F >80:
            print("It is too hot outside")
        elif F <60:
            print("It is chilly outside")
        else:
            print("It is very pleasent outside")
    else:
        print("")
        
        
else:
    print("Invalid units entered.Exiting")
    exit()
