name = input("What is your name? : ")
age = int(input("what is your age, {0} ? :".format(name)))

if age < 18:
    print("{0} , you are under-age. please comeback in {1} years.".format(name,18-age))
elif age > 100:
    print("You should die now {0}.".format(name))
else:
    print("You can vote, {0}.".format(name))


