from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the silent auction.")
input("The bid is about to start enter any key to continue: ")

continue_bid = True
bid_dict = {}

while continue_bid:

    clear()

    name = input("What is your name?: ")
    bid = input("What is your bid? £ : ")
    bid_dict[name] = float(bid)
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")

    if next_bidder == "yes":
        continue_bid = True
    else:
        continue_bid = False

max_bid = max(bid_dict, key=bid_dict.get)

print(f"{max_bid} won with a bid of £{bid_dict[max_bid]}!")

#Challenge: is to create a dictionary, where each person's name is the key and their bid will be the value

#after each bid is inputted, the user should be able to type 'yes' if there is someone else yet to bid or 'no' if they are the last bidder.

#if the user clicks 'yes' the console should clear() so their bid remains a secret and if they answer 'no' the highest bidder and their bid can be printted.

# the last step will require the program to loop through the dictionary to find the highest value/bid
