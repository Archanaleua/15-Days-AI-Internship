print("===== FOR LOOP =====")

for i in range(5):
    print("Number:", i)


print("\n===== FOR LOOP WITH START AND END =====")

for i in range(1, 6):
    print(i)


print("\n===== FOR LOOP WITH STEP =====")

for i in range(0, 11, 2):
    print(i)


print("\n===== WHILE LOOP =====")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1


print("\n===== NESTED LOOP =====")

for i in range(1, 4):
    for j in range(1, 4):
        print("i =", i, "j =", j)


print("\n===== LOOP THROUGH STRING =====")

name = "Archana"

for letter in name:
    print(letter)


print("\n===== BREAK =====")

for i in range(10):
    if i == 5:
        break

    print(i)


print("\n===== CONTINUE =====")

for i in range(10):
    if i == 5:
        continue

    print(i)


print("\n===== PASS =====")

for i in range(5):
    pass

print("Pass statement executed")