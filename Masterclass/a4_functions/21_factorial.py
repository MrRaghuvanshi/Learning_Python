# write a function for factorial and print factorial for 0 to 35 using loop

def factorial(value : int):
    if value !=0:
        i = 1
        fact = 1
        while i <= value:
            fact = fact * i
            i += 1
        return int(fact)

    else : return int(1)


# fact = factorial(5)
# print(fact)

for i in range(0, 35):
    print(factorial(i))


# def factorial(n: int) -> int:
#     """
#     Return n! (0! is 1).
#
#     Valid for `n` in the range 0 to 998 (inclusive).
#     Larger values of `n` will cause a RecursionError.
#     """
#     if n <= 1:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# for i in range(36):
#     print(i, factorial(i))