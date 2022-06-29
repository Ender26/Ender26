import time
import random

print("Hello and welcome to my hangman")
time.sleep(2)
print("Rools are simple: I have a word in my mind and you have to guess it")
time.sleep(2)
print("Lets begin")
time.sleep(2)
print("You have 5 lives")
#------------------------------------------

words  = ["bad" , "red" , "blue" , "cube" , "table"]

haveToGuess = random.choice(words) 

if len(haveToGuess) == 3:
    dashes = ["-","-","-",]
elif len(haveToGuess) == 4:
    dashes = ["-","-","-","-",]
elif len(haveToGuess) == 5:
    dashes = ["-","-","-","-","-",]

print(dashes)

letters = list(haveToGuess) 
lives = 5

playing = "yes" 
while playing == "yes":
    answer = input("Type your answer(type a letter)")
    if answer in letters:
        i = int(letters.index(answer)) 
        print(answer, " is in the word")
        dashes[i] = answer 
        print(dashes)
    else:
        lives= lives-1
        print(answer , " is not in the word - now you have ", lives," lives")
    if lives == 0:
        print("You lost, the word was " , haveToGuess, ", you managed to guess only ", dashes)
        playing = "no"
    if "-" not in dashes:
        print("Congrats you won")
        playing = "no"