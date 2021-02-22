#print table for 0 to 5


for i in range(1,6):
    for j in range(1,11):
        print("{0} times {1} is : {2}".format(i, j, i*j))
    print("-"*30)