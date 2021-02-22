#Working with list

list_1=['robin','pankaj','vipin', 'DJ', 'sandeep','pabitra']
list_2=['senbaga','aravind','maiyetree','vikas']
print(list_1)                   #print the whole list

list_1[2]='indrani'             #replaced 'vipin with 'indrani'
print(list_1)

print(list_1[2:4])              #it print  [2]: pankaj and [3]:indrani but not [4]

print(list_1[3:])               #it will print [3] and till end of the list

list_1.insert(4, 'prosenjit')   #inserted 'prosenjit' at [4] position
print(list_1)

list_2.extend(list_1)           #block .clear function to see it working, it is merging of 2 list.
print(list_2)

print(list_2.index('senbaga'))  # .index function helps to find out the index of particular object

copy_list=list_1.copy()+list_2.copy()
print(copy_list)                # .copy function copy the list into another list

list_1.clear()                  #cleared the list
print(list_1)

