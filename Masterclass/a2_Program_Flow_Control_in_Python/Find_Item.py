shopping_list = ["eggs", "milk", "bread", "sugar", "rice"]

find_item = "sugar"
i = None

#for i in range(5)
for i in range(len(shopping_list)):
    if shopping_list[i] == "sugar":
        print("{} found at position {}".format(find_item,i))
        break


#now write same code if item is not found
item = "banana"
index = None

for j in shopping_list:
    if item == shopping_list.index(j):
        index = j

if j is None:
    print(f"{item} found at position {index}")
else:
    print(f"{item} not found")

