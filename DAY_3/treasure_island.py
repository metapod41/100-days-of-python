print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************''')

print("Welcome to the treasure island\nYour mission is to find the treasure")
dir = input("Choose a direction where you want to go LEFT or RIGHT: ")
if dir=="LEFT" or dir=="left":
    boat=input("You have come accross a lake\ndo you want to wait for the boat or swim?: ")
    if boat=="wait" or boat=="WAIT":
        door = input("You have come accross three doors choose one to continue your journey RED BLUE or YELLOW: ")
        if door=="YELLOW" or door=="yellow":
            print("YOU WIN!!")
        elif door =="RED" or door=="red":
            print("Burned by fire\nGame over")
        elif door=="BLUE" or door == "blue":
            print("eaten by beasts\nGame over")
        else:
            print("Game over")
    else:
        print("you have been eaten by crocodiles\nGame over")
else:
    print("you fell in a hole\nGame over")
