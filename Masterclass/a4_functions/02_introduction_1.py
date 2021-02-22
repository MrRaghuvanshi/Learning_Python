def multiply(x, y):
    result = x * y
    return result


answer1 = multiply(2, 5)
print(answer1)

answer2 = multiply(int(input("enter value")), int(input("enter value")))
print(answer2)
print()

for val in range(1, 5):
    table_of_two  = multiply(2,val) #calling function in loop
    print(table_of_two)