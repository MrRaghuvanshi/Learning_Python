# for i in range(10):
#     print(f"i is now : {i}")



i = 0
while i<10:
    print(f"i is now : {i}")
    i+=1

print()

directions = ["east", "west", "north", "south"]
entry = ""

while entry not in directions:
    entry = input("select the direction : ")
    if entry.casefold() == "quit":
        print("I Quit!!!!")
        break

print("you are out of the loop")



