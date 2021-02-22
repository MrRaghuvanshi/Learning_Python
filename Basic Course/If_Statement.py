#using if statement with boolean variables

A = False
B = True
C = True
D = False

if A:
    print("A is true")              #not if front of variable is like "if B is not true then:"
elif not B:                         #elif is used when previous condition is not true.
    print("B is false")
else:                               #else come alone and there will be no condition in front of it.
    print("C is true")

#using if statement with integer variable

var1 = 1
var2 = 2
var3 = 3

if var1==var2!=var3:        #here python will check whether var 1 is equal to var2 and var2 is not equal to var3
    print("yes")            #turn var2 = 1 then you will get "true"
else:
    print("no")