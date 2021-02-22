def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string.casefold() == string[::-1].casefold()

sentence = input("enter sentence to check whether it is palindrome, or not : ")

if palindrome_sentence(sentence):
    print("'{}' is palindrome sentence.".format(sentence))
else:print("No, its not palindrome")
