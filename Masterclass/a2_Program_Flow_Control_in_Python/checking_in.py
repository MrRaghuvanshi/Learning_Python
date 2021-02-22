parrot = "Norwegien Blue"

letter = input("Enter a letter : ")

if letter in parrot:
    print("{0} is in {1}".format(letter,parrot))
else:
    print("No match")


