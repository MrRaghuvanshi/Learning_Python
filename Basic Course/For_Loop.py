
names=["apple", "banana","mango", "cherry"]
for fruite in names:
    print(fruite)
else: print("printing finished")


for fruite in names:
    print(fruite)
    if fruite=="banana":
        print("breaks at banana, and didint print further")
        break                               #it will break the loop if above condition is true

for fruite in names:
    if fruite=="banana":
        print("skiped banana, and moved further")
        continue
    print(fruite)

for number in range(6):
    print(number)           #print 0 to 5 using range function

for number in range(20,30):
    print(number)           #print 20 to 29