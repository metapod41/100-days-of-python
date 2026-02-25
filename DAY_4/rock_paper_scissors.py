import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

choice = int(input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): "))

if choice < 1 or choice > 3:
    print("Invalid choice")
else:
    user_choice = options[choice - 1]
    comp_choice = random.choice(options)

    print("You chose:")
    print(user_choice)
    print("Computer chose:")
    print(comp_choice)

    user_index = choice - 1
    comp_index = options.index(comp_choice)

    if user_index == comp_index:
        print("Draw")
    elif (user_index - comp_index) % 3 == 1:
        print("You win")
    else:
        print("You lost")

