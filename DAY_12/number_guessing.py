import random
from art import logo
def game():
    print(logo)
    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 to 100")
    number = random.randint(1,100)
    difficulty = input("Choose difficulty 'easy' or 'hard': ").lower()
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    won = False
    while attempts>0 and won is not True:
        print(f"You have {attempts} attempts remaining")
        guess = int(input("Guess a number between 1 to 100: "))
        if guess > number:
            print("Too high")
            attempts -= 1
        elif guess < number:
            print("Too low")
            attempts -= 1
        else:
            print("You guessed it right")
            won = True

    if attempts==0:
        print(f"You Lost , the number was {number}")

    again = input("Do you want to play again 'y' or 'n': ")
    if again == 'y':
        game()
    else:
        return
    
game()
    