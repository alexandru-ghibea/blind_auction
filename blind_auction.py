from logo import logo
from IPython.display import clear_output

print(logo)

bids = {'ana': 2}

bidding_finished = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f' Winner is {winner} with amount of  {highest_bid}')


while not bidding_finished:
    name = input("Please provide name: ")
    bid_price = int(input("Please provide bid amount:$ "))
    bids[name] = bid_price
    choice = input("Are there other users that want's to bid? Y or N: ").lower()
    if choice == "n":
        bidding_finished = True
        find_highest_bid(bids)
        break
    elif choice == "y":
        clear_output()

print(bids)
