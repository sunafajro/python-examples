listValue = ["R1", "R2", "R3", "R4"]

print(listValue[3])
print(listValue[-2])
print(listValue[2:4])

del listValue[2]
print(listValue)

listValue.append("R5")
print(listValue)

newList = listValue
listValue.insert(1, "R6")
print(newList, listValue)

newList = listValue[:]
del listValue[2]
print(newList, listValue)