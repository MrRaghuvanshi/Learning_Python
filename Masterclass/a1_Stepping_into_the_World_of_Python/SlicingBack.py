
letter= "abcdefghijklmnopqrstuvwxyz"
backward = letter[25::-1]
backward1= letter[::-1]             #::-1 is a Python idiom
print(backward)
print(backward1)

#task 1. produce "qpo"  2. produce "edcba"  3:last 8 letters in reverse order

task1 = letter[16:13:-1]
print(task1)

task2 = letter[4::-1]
print(task2)

task3_1 = letter[25:17:-1]
task3_2 = letter[:-9:-1]
print(task3_1)
print(task3_2)
