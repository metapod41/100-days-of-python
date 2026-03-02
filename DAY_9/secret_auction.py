import os
from art import logo
more = True
dict={}
print(logo)
while more:
    name = input("Enter your name\n")
    bid = int(input("Enter you bidding amount\n$"))

    dict[name]=bid

    again = input("Are there more persons to bid, Type 'y' if yes otherwise type 'n':\n-->")
    if again=='n':
        more=False
        os.system('cls')
    else:
        os.system('cls')

maxbid = 0
maxbidder=""
for name in dict:
    if dict[name]>maxbid:
        maxbid=dict[name]
        maxbidder=name

print(f"{maxbidder} won with the maximum bid of ${maxbid}")