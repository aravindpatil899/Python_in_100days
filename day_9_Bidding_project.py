#Project on Bidding
print("Welcome for Auction::\n")

auction_start =True
bidder_details = {}
while auction_start:
    name = input("what is your name : ")
    bid = int(input("what is your bid ? : $ "))
    next_bidder = input("Are there any other bidders ? Type yes or no : ").lower()
    bidder_details[name] = bid
    if next_bidder=='no':
        auction_start=False
max=0
highest_bidder=''
for key in  bidder_details:
    if bidder_details[key]>max:
        max=bidder_details[key]
        highest_bidder=key
print(f'{highest_bidder} wins the auction by bidding {max}')

