a = int(input("please enter 1st number"))
b = int(input("please enter 2nd number"))
for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print("this integer is divisible by both a and b", i)
        break