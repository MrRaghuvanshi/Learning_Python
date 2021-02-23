def fibonacci():
    value = input("enter a number for fibonacci : ")
    i = j = 0
    while i < int(value):
        j = j + (j + 1)
        i += 1

    return j


x = fibonacci()
print(x)
