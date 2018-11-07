'''
documentation
'''

import random
secret = random.randint(1, 99)

guess = 0
tries = 0
print("Can you guess my number?")
print("My number is an integer between 1 and 99!")

while guess != secret and tries < 6 :
    print("What is your guess?")
    guess = int(input())
    if guess < secret :
        print("Too Low")
    elif guess > secret :
        print("Too High")

    tries = tries + 1

if guess == secret:
    print("Your are correct! NOOB!")
else :
    print("Your out of guesses! try again")
    print("the secret numer was : ", secret)
