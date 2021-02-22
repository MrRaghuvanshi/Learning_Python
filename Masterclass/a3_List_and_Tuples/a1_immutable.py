
result = True
result_1 = result

print(id(result))
print(id(result_1))

result = False
print(id(result))               #we got differnt id for result because we changed the variable from true to false
print(id(result_1))
