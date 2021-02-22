
name = input("Hello Sir What is Your Name? :")
item = input("Hello Mr. "+name + " What did you buy today? :")
quantity = input("How many " +item + " did you buy ? :")
amount = input("Please tell the price of " + item + " ")

#input from user always gives string value, so for calculation, we have to convert it into float

total = print("You have to pay " + str(float(quantity)*float(amount)))