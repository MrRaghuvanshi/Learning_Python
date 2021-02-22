import random

number = random.randint(1,10)           #todo: remember the function of this comemnt
guess = int(input("Please guess the number : "))

if guess != number:
    if guess > number:
        print("{0} is higher. Please guess again".format(guess))
    else:
        print("{0} is lower. Please guess again".format(guess))
    guess2 = int(input())
    if guess2 == number:
        print("This time you guessed it  correct.")
    else:
        print("2nd time also wronged. WTF man")
else:
    print("You guessed it correct")