odd = [1,3,5,7,9]
even = [2,4,6,8]

print(odd)
print(even)

odd.extend(even)        #attaches the even list in front of odd
print(odd)

odd.sort()              #sort the list
print(odd)

odd.sort(reverse=True)  #reverse the list
print(odd)

name=["robin",
      "Indrani",
      "pankaj",
      "Prosenjit",
      "raverkar",
      "Sandeep",
      "dhananjay",
      "pabitra",
      "sachin"]



name.sort(key=str.casefold)

print(name)