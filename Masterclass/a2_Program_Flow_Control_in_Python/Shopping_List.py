
shopping_list = ["eggs", "milk", "bread", "sugar", "rice"]

#exclude sugar from buying

# for i in shopping_list:
#     if i != "sugar":
#         print("buy " + i)


for i in shopping_list:
    if i == "sugar":                #this code will not execute untill the conditions met
        continue                    #when the conditions met "continue" takes the program to line 11 again

    print("buy " + i)