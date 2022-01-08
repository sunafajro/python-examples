var = {"R1": "10.1.1.1", "R2": "10.2.2.2"}

print(var)

print(var["R1"])

var["R3"] = "10.3.3.3"
print(var)

del var["R2"]
print(var)

newVar = var
var["R4"] = "10.4.4.4"
print(newVar, var)

newVar = var.copy()
del var["R4"]
print(newVar, var)