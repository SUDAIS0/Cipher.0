logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

import random

print("Wellcome to black-jack game ")

cards = ["ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "jack" , "queen" , "king"]
cardsValue = {
    "ace" : 1 ,
    "2" : 2 ,
    "3" : 3 ,
    "4" : 4 ,
    "5" : 5 ,
    "6" : 6 ,
    "7" : 7 ,
    "8" : 8 ,
    "9" : 9 ,
    "10" : 10 ,
    "jack" : 10 ,
    "queen" : 10 ,
    "king" : 10
}

def cardsDelting():
    return cards[random.randint(0,12)]

def cardValue(cardsign):
    return cardsValue[cardsign]

def playerCards():
    playerCardList = [cardsDelting() , cardsDelting()]
    sum1 = 0
    for n in playerCardList:
        sum1 += cardValue(n)
    if ("ace" in playerCardList):
                sum1 += 10
    print(f"\n\t Your cards are {playerCardList} \t Thier sum is = {sum1}  ")

    flag = True
    
    while flag :
        choice = input("\n\t You want to HIT or STAND = ").lower()
        if(choice == "hit"):
            playerCardList.append(cardsDelting())
            sum1 = 0
            for n in playerCardList:
                sum1 += cardValue(n)
            if ("ace" in playerCardList) and sum1 < 12:
                sum1 += 10 
            print(f"\n\t Your cards are ({playerCardList}) \t Thier sum is = {sum1}")
            if sum1 >= 21 :
                flag = False
        elif(choice == "stand"):
            flag = False
        else:
            print("\n\t Error \n\t Wrong inputs")
        
    return sum1
         
def dealersCard():
    dealerCardList = [cardsDelting() , cardsDelting()]
    sum2 = 0
    for n in dealerCardList:
        sum2 += cardValue(n)
    if ("ace" in dealerCardList):
                sum2 += 10
    while sum2 < 17 :
        dealerCardList.append(cardsDelting())
        sum2 = 0
        for n in dealerCardList:
            sum2 += cardValue(n)
        if ("ace" in dealerCardList) and sum2 < 12:
                sum2 += 10
    if sum2 > 21 :
                print(f"\n\t Dealer cards are ({dealerCardList}) \t Thier sum is = {sum2}")
                return sum2
    print(f"\n\t Dealer cards are ({dealerCardList}) \t Thier sum is = {sum2}")
    return sum2

flags = True

while flags :
    play = input("\n Do you want to play (yes/no)= ").lower()
    if play == "yes":
        playerCardsValue = playerCards()
        dealersCardValue = dealersCard()

        if playerCardsValue > 21 :
            print("\n\t Error \n\t ***Your Busted*** \n\t ***You Lost***")
        elif dealersCardValue > 21 :
            print("\n\t Congratulations \n\t ***You Won***")
        elif playerCardsValue > dealersCardValue :
            print("\n\t Congratulations \n\t ***You Won***")
        elif playerCardsValue < dealersCardValue :
            print("\n\t Error \n\t ***Your Busted*** \n\t ***You Lost***")
        else:
            print("\n\t Draw \n\t ***Pushing bets***")
    elif play == "no":
        flags = False
    else:
        print("\n\t Error \n\t Wrong inputs")