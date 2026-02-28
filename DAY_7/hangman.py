import random
from words import word_list
from stage import stages,logo

print(logo)
lives = 6
i = 0
chosen_word = random.choice(word_list)


to_guess = ""
for char in chosen_word:
    to_guess+='_'
print(to_guess)

word_len = len(chosen_word)
correct=[]
game_over = False

while(not game_over):
    print(f"**************YOU HAVE {lives}/6 LIVES REMAINING********************")
    guess = input("Guess a word\n").lower()
    if guess in correct:
        print(f"you already guessed {guess}")
    
    res = ""
    if guess not in chosen_word:
        lives -= 1
        print(f"your guessed word {guess} is not correct. You lost a life")
    

    for char in chosen_word:
        if char == guess:
            res+=guess
            correct.append(guess)
        elif char in correct:
            res+=char
        else:
            res+='_' 

    if guess in chosen_word:
        print(stages[i])
    else:
        i += 1
        print(stages[i])
    print(res) 
    
    if lives == 0:
        game_over = True
        print("***********************YOU LOST****************************")
        print(f"correct word was {chosen_word}")
    if '_' not in res:
        game_over = True
        print("***********************YOU WON*****************************")
          
    