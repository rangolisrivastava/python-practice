a = int(input("enter the number"))
b = int(input("enter the number"))
c = input("enter the operator")

if (c == "+"):
    print("sum:", a + b)
elif (c == "-"):
    print("diff:", a - b)
elif (c == "*"):
    print("product:", a * b)
elif (c == "/"):
    print("division:", a / b)
elif (c == "**"):
    print("power:", a ** b)
elif (c == "%"):
    print("remainder:", a % b)
else:
    print("invalid operator")
