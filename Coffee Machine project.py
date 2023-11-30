logo = """
           __    __   __  __    __    ___   ___           __            
          / / /\ \ \ /__\/ /   / /   / __\ /___\ /\/\    /__\           
          \ \/  \/ //_\ / /   / /   / /   //  ///    \  /_\             
           \  /\  ///__/ /___/ /___/ /___/ \_/// /\/\ \//__             
            \/  \/ \__/\____/_____/\____/\___/ \/    \/\__/             
                            /__   \ /___\                               
                              / /\///  //                               
                             / /  / \_//                                
   ___   ___   ___  ___  __  __   \_____  __    __    _        __   ___ 
  / __\ /___\ / __\/ __\/__\/__\   \_   \/ _\  / /   /_\    /\ \ \ /   \\
 / /   //  /// _\ / _\ /_\ /_\      / /\/\ \  / /   //_\\  /  \/ // /\ /
/ /___/ \_/// /  / /  //__//__   /\/ /_  _\ \/ /___/  _  \/ /\  // /_// 
\____/\___/ \/   \/   \__/\__/   \____/  \__/\____/\_/ \_/\_\ \//___,'  
"""
print(logo)

flavours = [
{
    "coffee type" : "Espresso" ,
    "water required" : 50 ,
    "milk required" : 0 ,
    "coffee required" : 18 ,
    "money required" : 1.50
},
{
    "coffee type" : "Latte" ,
    "water required" : 200 ,
    "milk required" : 150 ,
    "coffee required" : 24 ,
    "money required" : 2.50
},
{
    "coffee type" : "Cappuccino" ,
    "water required" : 250 ,
    "milk required" : 100 ,
    "coffee required" : 24 ,
    "money required" : 3.00
}
]
thingsInStock = ["water" , "milk" , "coffee" , "money"]

stock = {
    "water" : 500 ,
    "milk" : 500 ,
    "coffee" : 100 ,
    "money" : 0
}

coinName = ["QUATERS" , "DIMES" , "NICKELS" , "PENNIES"]

coins = {
    "QUATERS" : 0.25 ,
    "DIMES" : 0.10 ,
    "NICKELS" : 0.05 , 
    "PENNIES" : 0.01
}

coffeeType = {}
totallMoney = 0


def userChoice():
    global coffeeType
    flags = True
    while flags :
        choice = int(input("\n\t Which coffe whould you like \n\t 1: Espresso \t Price : 2.5\n\t 2: Latte \t Price : 1.25\n\t 3: Cappuccino \t Price : 1.75\n\n\tWrite number ==>"))
        if choice < 4 and choice > -1 :
            flags = False
        else:
            print("\n\t\t Error \n\t Invalid input")
    choice -= 1
    coffeeType = flavours[choice]
    return coffeeType


def checkRequirments():
    global stock
    choice = userChoice()
    if choice["water required"] >= stock["water"]:
        print("\n\t\t SORRY \n\t Not enough WATER")
    elif choice["milk required"] >= stock["milk"]:
        print("\n\t\t SORRY \n\t Not enough MiLK")
    elif choice["coffee required"] >= stock["coffee"]:
        print("\n\t\t SORRY \n\t Not enough WATER")
    else:
        stock["water"] -= choice["water required"]
        stock["milk"] -= choice["milk required"]
        stock["coffee"] -= choice["coffee required"]
        return True


def insertMoney():
    global totallMoney
    moneyRequired = coffeeType["money required"]
    coinname = 0
    while coinname != 4 :
        moneyInserted = float(input(f"\n\t How many of {coinName[coinname]} have you inserted (type 0 if none) = $"))
        totallMoney += coins[coinName[coinname]] * moneyInserted
        coinname += 1
        print(f"\n\t Youe current inserted money is = ${round(totallMoney , 2)}")
    if (totallMoney >= moneyRequired):
        if (totallMoney > moneyRequired):
            returnMoney = totallMoney - moneyRequired
            totallMoney -= returnMoney
            stock["money"] += totallMoney
            totallMoney = 0
            return returnMoney
        stock["money"] += totallMoney
        totallMoney = 0
        return 0
    print("\n\t Error \n\t Not enough money \n\t Insert more money")
    insertMoney()


def stockInfo():
    print(f"\n\t You'r current stock of ingredients in the machine are \n\t Water : {stock["water"]} \n\t Milk : {stock["milk"]} \n\t Coffee : {stock["coffee"]} \n\t Money : {stock["money"]}")
    flagg = True
    while flagg :
        insert1 = input("\n\t You want to add any thing in the machine (yes/no)= ").lower()
        if insert1 == "yes" :
            flag = True
            while flag :
                insert2 = int(input("\n\t What do you want to insert \n\t 1: Water \n\t 2: Milk \n\t 3: Coffee \n\t ==>>"))
                if insert2 > -1 and insert2 < 4 :
                    ingredient = thingsInStock[insert2-1]
                    amount = int(input("\n\t How much amount do you want to add = "))
                    (stock[ingredient]) += amount
                    flag = False
                else:
                    print("\n\t\t Error \n\t Invalid input")
        elif insert1 == "no" :
            flagg = False
        else:
            print("\n\t\t Error \n\t Invalid input")


def main():
    flag = True
    while flag :
        oder = input("\n\t\t Hi! There We Serve A Great Coffee \n\n\n\t Do you want oder (yes/no) \n\t\t [Type check to check the igredients of the machine (only admin)(password required)] \n\n\t==>> ").lower()
        if oder == "yes" :
            if checkRequirments() :
                returnMoney = insertMoney()
                print(f"\n\t Here's You'r {coffeeType["coffee type"]} Coffee \n\t Have a Great Day")
                if returnMoney != 0 :
                    print(f"\n\t Here's You'r ${round(returnMoney , 2)} Change")
        elif oder == "check" :
            password = input("\n\t Type password ==>> ").lower()
            if password == "sudais" :
                stockInfo()
            else:
                print("\n\t\t Error \n\t Invalid Passowrd")
        elif oder == "no" :
            flag = False
        else:
            print("\n\t\t Error \n\t Invalid input")


main()