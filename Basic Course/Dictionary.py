#creating a dictionary

color_dictionary = { "B":"Blue",
                     "Bl":"Black",
                     "R":"Red",
                     "O":"Orange",
                     "P":"Pink" }

print(color_dictionary.get("B", "Dont have such color in this dictionary"))
print(color_dictionary.get("C", "Dont have such color in this dictionary"))

#taking employee number from user and print the name of employee

employee_database={ 111:"Robin",
                    222:"Vipin",
                    333:"indrani",
                    444:"Pnakaj",
                    555:"Sandeep"}

roll_number=int(input("Enter the roll number of employee you are looking for : "))
print(employee_database.get(roll_number, "please enter valid roll number"))