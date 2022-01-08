fileName = "devices.txt"

def getDevices():
    file = open(fileName, "r");
    return file.readlines(10)

data = getDevices()
print(data)

def addNumbers(a, b = 1):
    return a + b

# print(addNumbers())
print(addNumbers(2))
print(addNumbers(3, 2))
print(addNumbers(1, b = 3))
print(addNumbers(b = 2, a = 1))