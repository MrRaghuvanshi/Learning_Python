shopping_list = ["eggs", "milk", "bread", "sugar", "rice"]

print(id(shopping_list))


shopping_list+= ["potato"]          #adding new item
print(shopping_list)

print(id(shopping_list))            #id of shopping list doesn't change

shopping_list.append("cheese")      #append and adding new item at line 7 works same
print(shopping_list)