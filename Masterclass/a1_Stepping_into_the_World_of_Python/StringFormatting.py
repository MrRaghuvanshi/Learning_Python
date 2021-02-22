
for i in range(1 , 13):
    print("Square of {0} is {1} and cube is {2}".format(i,i**2,i**3))  #i**2 means i raise to 2

print()

for i in range(1 , 13):
    print("Square of {0:2} is {1:3} and cube is {2:4}".format(i, i ** 2, i ** 3))  # {0:2} will print with 2 characters

print()

for i in range(1 , 13):
    print("Square of {0:<2} is {1:<3} and cube is {2:<4}".format(i, i ** 2, i ** 3))  # left align

print("Approx. value of pi is {0}".format(22/7))
print("Approx. value of pi is {0:50}".format(22/7))
print("Approx. value of pi is {0:50f}".format(22/7))
print("Approx. value of pi is {0:0.50f}".format(22/7))
print()
print(f"Approx. value of pi is {22/7:0.50f}")           #f-string
print(f"my age is {26} year old")

