age = int(input("What is your age? :"))

# if age >=18 and age <=60: #this one, and below one, both conditions are same

if 18 <= age <= 60:
    print("You are eligible to work")
else:
    print("not eligible.")

print("-" * 80)

if 18 > age or 60 < age:
    print("not eligible.")
else:
    print("You are eligible to work")