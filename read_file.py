fileName = "devices.txt"

for name in open(fileName):
    if "Switch" in name:
        print(name.strip())

print("==========")

file = open(fileName, "r")
rows = file.readlines()
for row in rows:
    if "Router" in row or "Phone" in row:
        print(row.strip())
file.close()