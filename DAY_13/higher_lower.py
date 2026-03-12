import random
from data import data
import os
again = 'y'
def game():
    cont = True
    count = 0
    while(cont):
        

        a = random.choice(data)
        b = random.choice(data)
        

        print(f"A. {a['name']} , {a['description']} , {a['country']}")
        print("VS")
        print(f"B. {b['name']} , {b['description']} , {b['country']}")

        guess = input("Who is more famous A or B : \n").upper()
        if(guess=='A'):
            guess = a
            check = b
        else:
            guess = b
            check = a

        if(guess['followers']>check['followers']):
            print("Correct guess")
            count+=1
            print(f"Your current score is {count}")
        else:
            cont = False
            print("Wrong guess")
            print(f"Your final points: {count}")
            
   

while True:
    game()

    again = input("\nDo you want to play again (y/n): ").lower()

    if again != 'y':
        print("Goodbye")
        break




