var = int(input("Input a number: "))

if var < 2:
    print(f"{var} < 2")
elif var == 0:
    print(f"var == 0")
elif var > 6:
    print(f"{var} > 6")
elif var != 7:
    print(f"{var} != 7")
else:
    print(f"{var} > 2 and {var} < 6")