#print value 10 to 15

for i in range(10,16):
    print("i is now : {0}".format(i))

print()

for i in range(5):             #starting index will be 0, therefore it will print from 0 to 9
    print(i)

print()

for i in range(5,0,-1):       #reverse printing/counting
    print(i)

print()

for i in range(0,10,2):         #stepping by 2
    print(i)

print()

#write a program to pritn out all the numbers from 0 to 100 that are divisible by 7.

for i in range(0,101):
    if i%7==0:
        print(i)