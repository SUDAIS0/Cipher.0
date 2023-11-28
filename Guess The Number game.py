logo = """     
     /    ||  |  |  /  _]/ ___// ___/       
    |   __||  |  | /  [_(   \_(   \_        
    |  |  ||  |  ||    _]\__  |\__  |       
    |  |_ ||  :  ||   [_ /  \ |/  \ |       
    |     ||     ||     |\    |\    |       
    |___,______,________| ____| \___|       
        |      ||  |  |  /  _]              
        |      ||  |  | /  [_               
        |_|  |_||  _  ||    _]              
          |  |  |  |  ||   [_               
          |  |  |  |  ||     |              
 ____   __|__| _______||_____|   ___  ____  
|    \ |  |  ||   |   ||    \   /  _]|    \ 
|  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|  |  ||     ||   |   ||     ||     ||  .  \\
"""

print(logo)
import random

def number1():
    return random.randint(0, 100)

def number2():
    return int(input("\n\t Guess the number between 0 to 100 = "))

def compare(turns):
    num1 = number1()
    print(f"\n\t You have only {turns} tries.")
    while turns != 0:
        num2 = number2()
        turns -= 1
        if num1 < num2:
            print(
                f"\n\t The number you typed is HIGH \n\t Number of tries left = {turns}"
            )
        elif num1 > num2:
            print(f"\n\t The number you typed is LOW \n\t Number of tries left = {turns}")
        else:
            print(
                f"\n\t ***Congratulations*** \n\t You guessed the right number \n\t Number of turns left = {turns}"
            )
            turns = 0
            return
    print(f"\n\t You lost \n\t The number you was guessing is = {num1}")

turns = 10
flag = True

while flag:
    choice1 = input("\n\t You want to play the game (yes/no)= ").lower()
    if choice1 == "yes":
        flags = True
        while flags:
            choice2 = input("\n\t What kind of difficulty will you like (hard(5 tries)/easy(10 tries))= ").lower()
            if choice2 == "hard":
                turns = 5
                flags = False
                compare(turns)
            elif choice2 == "easy":
                flags = False
                compare(turns)
            else:
                print("\n\t Error \n\t Wrong intput")
    elif choice1 == "no":
        flag = False
    else:
        print("\n\t Error \n\t Wrong intput")