# It's a simple game, usually played with 2 or more people.
# If the number is divisible by 3, you say "fizz" instead.
# If it's divisible by 5, you say "buzz".
# And if it's divisible by both 3 and 5, you say "fizz buzz".
# function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's not divisible by either 3 or 5.
# The function will always return a string. When you return the number, therefore, you should convert it to a string first.


def fizz_buzz(value):
    if value % 5 == 0 or value % 3 == 0:
        if value % 3 == 0 and value % 5 ==0:
            return str("fizz buzz")
        elif value % 3 == 0:
            return str("fizz")
        elif value % 5 == 0:
            return str("buzz")
    else:
        return str(value)

entered_number = int(input("enter a number"))
answer = fizz_buzz(entered_number)
print(answer)


# def fizz_buzz(number: int) -> str:
#     """
#     Play Fizz buzz
#
#     :param number: The number to check.
#     :return: 'fizz' if the number is divisible by 3.
#         'buzz' if it's divisible by 5.
#         'fizz buzz' if it's divisible by both 3 and 5.
#         The number, as a string, otherwise.
#     """
#     if number % 15 == 0:
#         return "fizz buzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
#
#
# for i in range(1, 101):
#     print(fizz_buzz(i))