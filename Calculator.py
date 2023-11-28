logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def addition(digit1 , digit2):
    return digit1 + digit2
def subtraction(digit1 , digit2):  
    return digit1 - digit2

def multiplication(digit1 , digit2):
    return digit1 * digit2

def division(digit1 , digit2):
    return digit1 / digit2

def calculation(operation , digit1 , digit2):
    if(operation == "+"):
        return addition(digit1 , digit2)
    elif(operation == "-"):
        return subtraction(digit1 , digit2)
    elif(operation == "*"):
        return multiplication(digit1 , digit2)
    elif(operation == "/"):
        return division(digit1 , digit2)
    else:
        print("\n\t ERROR\n\tYou wrote invalid operation")

flag = True
flags = True

while flag :
    if flags:
        digit1 = float(input("Write the 1st digit = "))
        operation  = input("""What do you want to do :
                    \n\t+  -  *  /
                   \n\t Type one of the above = """)
        digit2 = float(input("Write the 2nd digit = "))
        print(calculation(operation , digit1 , digit2))
        flags = False
    choice = input("You want to continue with the current value (yes/no)(type terminate to end programe)= ").lower()
    if(choice == "yes"):
        digit1 = calculation(operation , digit1 , digit2)
        print(f"Now your first digit is = {digit1}")
        operation  = input("""What do you want to do :
                    \n\t+  -  *  /
                   \n\t Type one of the above = """)
        digit2 = float(input("Write the 2nd digit = "))
        print(calculation(operation , digit1 , digit2))
    elif(choice == "no"):
        flags = True
    elif(choice == "terminate"):
        flag = False
    else:
        print("\n\t ERROR\n\tYou wrote invalid command")