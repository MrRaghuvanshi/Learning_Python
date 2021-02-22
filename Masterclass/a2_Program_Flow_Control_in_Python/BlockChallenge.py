# change the condition to guess == answer (Block_1)

number = 5
guess = int(input("Please guess the number : "))

if guess == number:
    print("You guessed it correct")
else:
    if guess > number:
        print("{0} is higher. Please guess again".format(guess))
    else:
        print("{0} is lower. Please guess again".format(guess))
    guess2 = int(input())
    if guess2 == number:
        print("This time you guessed correct!!")
    else:
        print("2nd time also wronged. WTF man")





