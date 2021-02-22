
def abcd(name) :                    #User-Define functions
    print("My name is "+ name)

abcd("robin")                       #call functions


def hotel() :                                                   #here we are not assigning any parameter to function
   name=input("Hello Sir, What is your name? : ")
   age=input("Hello "+ name + ", What is your age? : ")
   city=input("from where you are coming? : ")
   advance=input("Do you want to pay any advance? : ")

hotel()

def hotel_1(name) :                                                   #here we are assigning any parameter to function
  print("Hello Sir, What is your name? : ")
  age=input("Hello "+ name + ", What is your age? : ")
  city=input("from where you are coming? : ")
  advance=input("Do you want to pay any advance? : ")

hotel_1("vipin")