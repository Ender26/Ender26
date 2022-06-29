import random
import time

number = random.randint(1 , 100)
guess = int(input("Enter a number: "))

while guess != number:
    if guess > number:
        print("Go Lower")
        time.sleep(1)
        guess = int(input("Enter a number: "))
    if guess < number :
        print("Go Higher")
        guess = int(input("Enter a number: "))
        time.sleep(1)
    if guess == number:
        print("You win")
        break
