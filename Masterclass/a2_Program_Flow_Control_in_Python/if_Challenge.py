name = input("What is your name? : ")
age = int(input("What is your age, {}? : ".format(name)))


#there are two ways to write the same code.

# if 18<= age <31:


if age in range(18, 32):
    print("Welcome to hotel, {}.".format(name))
else:
    print("You are not allowed to enter!!")




