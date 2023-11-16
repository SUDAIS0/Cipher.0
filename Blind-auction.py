logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

data = []


def bidders(bidder_name , bid):
    temp = {
        "BidderName" : bidder_name,
        "Bid" : bid
    }
    data.append(temp)



number_of_bidders = 1
flag = True
while (flag):
    bidder_name = input("What is your name = ")
    bid = input(f"Enter you bid Mr/Mrs {bidder_name} = $")

    bidders(bidder_name , bid)
    flagg = True
    while flagg:
        
        choice = input("\n\tYou want to place bid again ??\n\t Type yes to go again or no to stop  = ").lower()
        if(choice == "yes"):
            number_of_bidders += 1
            flagg = False
        elif (choice == "no"):
            flagg = False
            flag = False
        else:
            print("\t\t Typing Error\n\t Type the right instruction please")

highest = 0
for person in data:
    price = int(person["Bid"])
    if (highest <= price):
        highest = price
        name = person["BidderName"]

print(f"Totall numbers of bidders are = {number_of_bidders}")
print(f"The highest bid is placed by {name.upper()} which is ${highest}")