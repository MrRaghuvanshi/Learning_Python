#palindrome

def palindrome(string):
    backwards = string[::-1]
    return backwards == string


word = input("enter the word : ")
if palindrome(word):
    print("'{0}' is a palindrome ".format(word))
else: print("try another word")

