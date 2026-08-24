for i in range (1, 21, 2): #odd number from 1-20
    print(i)

for i in range(57, 571, 57): #table of 57
    print(i)

i = 3
while i <= 50: #multiple of 3 from 1 to 50 but skip 15
    if i == 15:
        i += 1 # The Escape Hatch
        continue #bcause continue force the code to skip the bottom i += 1, i never became 16 ie- trapped at 15 for eternity
    if i % 3 == 0:
        print(i)
    i += 1 #The Main Engine
print("End of the code") #Escape hatch comes in action only when i = 15 so that it further becomes 16 before skipping it, and for other int this whole if block is skipped with this escape hatch so the main engine is required.
#easier way is to use for 


