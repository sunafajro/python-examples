fileName = "dump.txt"

file = open(fileName, "w")
for i in range(1,10):
    file.write(f"R{i}\n")
file.close()

file = open(fileName, "a")
for name in ("R10", "R11",):
    file.write(f"{name}\n")
file.close()