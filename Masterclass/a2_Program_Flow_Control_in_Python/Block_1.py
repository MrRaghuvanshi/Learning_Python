number = 5

# guess = int(input("Please guess the number : "))
#
# if guess > number:
#     print("{0} is higher.".format(guess))
# elif guess < number:
#     print("{0} is lower.".format(guess))
# else:
#     print("You guessed it correct")


# guess = int(input("Please guess the number : "))
# if guess > number:
#     print("{0} is higher. Please guess again".format(guess))
#     guess2 = int(input())
#     if guess2 == number:
#         print("This time you guessed it  correct.")
#     else:
#         print("2nd time also wronged. WTF man")
#
# elif guess < number:
#     print("{0} is lower. Please guess again".format(guess))
#     guess2 = int(input())
#     if guess2 == number:
#         print("This time you guessed it  correct.")
#     else:
#         print("2nd time also wronged. WTF man")
# else:
#     print("You guessed it correct")

#the above code also produce the same answer as below, but below one is more optimized way to write code

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
