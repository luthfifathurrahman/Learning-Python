def add_bidder(bidder_name, amount_bid):
  bid_list.append(
    {
      "name" : bidder_name,
      "amount" : amount_bid
    }
  )

def bidding_record():
  highest_bid = 0
  for i in range(len(bid_list)):
    winner_name = bid_list[i]["name"]
    winner_bid = bid_list[i]["amount"]
    if winner_bid > highest_bid:
      highest_bid = winner_bid
  print(f"The Winner is {winner_name} with a bid of ${highest_bid}")

import art
print(art.logo)
print("Welcome to the auction program.")
bid_list = []
bid_over = False

while not bid_over:
  name = input("What is your name? ")
  amount = int(input("What is your bid? $"))
  add_bidder(bidder_name=name, amount_bid=amount)
  any_bidder = input("Are there any other bidder? 'yes' or 'no'. ").lower()
  if any_bidder == "no":
    bid_over = True
    bidding_record()