def fibonacci(value: int) -> int:
    i = j = 0
    j_minus1 = 1
    while i < int(value):
        k = j + j_minus1
        j_minus1 = j
        j = k
        i += 1
    return k


x = fibonacci(input("enter a number for fibonacci : "))
print(x)
