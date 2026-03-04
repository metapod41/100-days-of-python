import random
from art import logo
import os
def deal_cards():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)



def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_score(u_score , c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score==0:
        return "You Lost computer had a BLACKJACK!!"
    elif u_score==0:
        return "You Won with a BLACKJACK!!"
    elif u_score>21:
        return "You went over.You Lost"
    elif c_score>21:
        return "Computer went over. You Won"
    elif u_score>c_score:
        return "You Won"
    else:
        return "You Lost"
def blackjack():    
    print(logo)
    user = []
    computer = []
    is_game_over=False
    user_score=-1
    computer_score=-1

    for i in range(0,2):
        user.append(deal_cards())
        computer.append(deal_cards())
        
    while(not is_game_over):
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)

        print(f"Your cards: {user} , cuurent score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            deal = input("type 'y' to get another card type 'n' to pass: ")
            if deal=='y':
                user.append(deal_cards())
            else:
                is_game_over=True

    while(computer_score != 0 and computer_score<17):
        computer.append(deal_cards())
        computer_score = calculate_score(computer)

    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"Your final hand : {user} , Your final score : {user_score}")
    print(f"Computer's final hand : {computer} , Computer's final score : {computer_score}")

    print(compare_score(user_score,computer_score))

    play_again = input("Type 'y' to play again or Type 'e' to exit: ")

    if(play_again=='y'):
        os.system('cls')
        blackjack()
    else:
        return 
    
blackjack()


