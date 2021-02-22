# we will ask user to guess a number and he have to give us direction whether our guess is correct or not

low = 1
high = 1000
guess = 0

print("Please think number in between 1 to 1000")
input("Press Enter to confirm!!!!")

while True:
    guess = low + (high - low) // 2

    print("\t guessing in range of {} to {}".format(low,high)) #TODO : cheking the code is working or not

    high_low = input("My guess is {}. \nTell me should I guess higher or lower. "
                     "if I should guess higher then press h, for lower press l. "
                     "if I guessed correct press c : ".format(guess))
    if high_low == "l".casefold():
        high = guess - 1

    elif high_low == "h".casefold():
        low = guess + 1

    elif high_low == "c".casefold():
        print("thank you for confirmation!! your number is {}".format(guess))
        break

    else:
        print("""Please enter letter "h", "l" and "c". """)
