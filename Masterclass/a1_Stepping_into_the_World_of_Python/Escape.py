print("\nwe can split\nlines by using\n")

print("tabbing\ttabbing\ttabbing\t1\t2\t3")

print("but you can use \" in this argrument also by using \ in front of \" ")

print("""\nyou can use 3 " to avoid any escape function we used in above line, we can use ' and  " both.""")

A="""split
the
line"""

#here by adding \ we can escape the new line

AA="""split\
the\
line"""
print(A)
print(AA)

print("C:\\User\\robin\\notes.txt")         #we used \, 2 times to escape the \n and \r escapes
print(r"C:\User\robin\notes.txt")           #we used r in front of argument to make it raw string
