data = []

while True:
    text = input("Write device name: ")
    if text.lower() == "exit":
        break
    data.append(text)

print(data)