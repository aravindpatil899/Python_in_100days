#project on hang man
"""generate random word --> guess the word ..letter by letter-->for every wrong letter hangman drawing """
import random 
import hangman_art
from hangman_wordlist import word_list

word = random.choice(word_list)
word_len = len(word)
blanks=''
display=''
correct_letters = []
print(word)
print(blanks)
tries = 0
game_over =False
lives=6
while not game_over:
    display=''
    guess = input('guess a letter :')    
    for letter in word :          
        if guess == letter:
            display +=guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display +=letter
        else:
            display +='_'         
    word_len -=1
    print(display)
    if guess not in word:
        lives-=1 
        if lives ==0:
            game_over=True
            print("=====You Loose===================")
    if "_" not in display:
        game_over =True
        print("============You Win============ ")
    print(correct_letters)
    print(hangman_art.hangman[lives])
