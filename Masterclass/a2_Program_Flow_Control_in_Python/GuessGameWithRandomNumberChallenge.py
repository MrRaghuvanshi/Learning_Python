# generate a random number and ask user to guess the number andput user into while loop
#until the answer is not correct he will be in loop
#user can quit using "0"
#count the number of attempts


import random

number = random.randint(1,10)
guess = None
print(number)                       #todo: remember the remove this
number_of_attempt = 0

while guess != number:
    guess = int(input("Please guess the number : "))
    number_of_attempt += 1

    if guess == 0:                      #for quiting the game
        break

    if guess > number:
        print("{0} is higher. Please guess again".format(guess))
    elif guess < number:
        print("{0} is lower. Please guess again".format(guess))
    else:                               #fior guessing the number correct
        print("You guessed it right!!!!, you took {} attempts".format(number_of_attempt))
        break


