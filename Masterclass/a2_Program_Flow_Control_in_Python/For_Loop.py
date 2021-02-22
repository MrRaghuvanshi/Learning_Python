name = "robin singh"

for i in name:                  #for loop assign each character in "name" to "i" and prints
    print(i)                    #for better understanding run program in debuger


#lets find out how many special character is in string

complex_string = "123,13,13;13.94-924"
special_char = ""

for i in complex_string:
    if not i.isnumeric():
        special_char = special_char + i

print(special_char)



quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

capital = ""

for i in quote:
    if i.isupper():
        capital = capital + i
print(capital)