numbers = [1, 6, 9, 31, 67]

for i in numbers:
    if i % 10 == 0:
        print("numbers are not ok")
        break
else:                               #if you look at the identation of else, it is with for loop
    print("numbers are ok")



