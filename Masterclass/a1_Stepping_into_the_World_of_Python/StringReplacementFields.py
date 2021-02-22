age = 26
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))
#replacement field is represented by the left curly brace the 0 and the right
#curly brace, which is then replaced by the first value in the format list,
#age in this case. And at the moment we've only got the one value in there and
#that's the variable age.

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "March", "May", "July", "Aug", "Oct", "Dec"))

print("Yuvraj Singh Hit {0}, {0}es in {1}th over of struart broad".format(6,4))


