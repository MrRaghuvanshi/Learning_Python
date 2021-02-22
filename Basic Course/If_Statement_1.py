#let's find out who is oldest person, we'll ask eachone thier name and age.

person1_name=input("Hello tell me your name, please : ")
person1_age=float(input("hello Mr. "+ person1_name+ ", what is your age? : " ))
person2_name=input("Hello tell me your name, please : ")
person2_age=float(input("hello Mr. "+ person2_name+ ", what is your age? : " ))
person3_name=input("Hello tell me your name, please : ")
person3_age=float(input("hello Mr. "+ person3_name+ ", what is your age? : " ))

oldest= max(person1_age,person2_age,person3_age)

if oldest==person1_age:
    print("the oldest person is : "+person1_name)
elif oldest==person2_age:
    print("the oldest person is : "+person2_name)
else:
    print("the oldest person is : "+person3_name)