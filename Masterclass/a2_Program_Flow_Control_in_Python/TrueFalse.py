day = "Monday"
Temperature = 25
Raining = False

if (day == "Monday" and Temperature == 25) or not Raining:
    print("Good day")
else:
    print("bad day")

if 0:                           #if statement evaluates the value with Zero "0"
    print("ABCD")
else:
    print("XYZ")


name=input("Enter your name : ")
if name:                            # if you enter blank name then if statement will comaapre with null string ie ""
    print("Hello, {}!!".format(name))
else:
    print("Don't you have name?")