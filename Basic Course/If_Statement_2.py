#lets test covid-19 checklist

def Covid_Test():
    Name= input("What is your name? : " )
    Age = float(input("What is your age? : "))

    cough= input("Do you have cough? yes/no : ")
    if cough.lower() == "yes":        #user input case sensitiveness doesnot matter, we are changing it in lower case
        return print("you need to have a test for covid-19")
    else: print("ok, next question.")

    fever=input("Do you have any fever? yes/no : ")
    if fever.lower()=="yes":
       return print("you need to have a test for covid-19")
    else: print("ok, next question.")

    chest_pain=input("Do you have chest pain? yes/no : ")
    if chest_pain.lower()=="yes":
        return print("you need to have a test for covid-19")
    else: print(" Sir, you are ok, thank you for doing screening")
    return

Covid_Test()



