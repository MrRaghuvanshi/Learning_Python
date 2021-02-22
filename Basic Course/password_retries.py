#we have to block user if dont put right passwords 3 times in a row


password="1234password"
number_of_attemmpts=3

max_number_of_retires=3

password_entered=input("you have 3 tries, please enter your password : ")

while password_entered!=password:
    number_of_attemmpts = number_of_attemmpts - 1
    if number_of_attemmpts==0:
         print("your account is blocked!!!!")
         break


    print("wrong password!, number of attempt left is "+str(number_of_attemmpts))
    password_entered = input("please enter correct password : ")

if password_entered == password:
    print("you entered correct password, congratulations!")




