# #Task1
print("Task1")
radok = input("Введіть будь-який рядок: ")
print("Вивід рядка поелементно: ")
print(radok[:])

#Task2
print("Task2")
radok = input("Введіть рядок для 2го завдання (шукає максимальну кількість символів підряд): ")
symb = radok[0]
symbCount = 1
maxSymbCount = 0
for i in range(1, len(radok)):
    if (radok[i-1] == radok[i]):
        symbCount += 1
    else:
        symbCount = 1

    if (symbCount > maxSymbCount):
        maxSymbCount = symbCount
        symb = radok[i]

print(symb)
print(maxSymbCount)

#Task3
print("Task3")
radok = input("Введіть рядок для третього завдання (декілька слів, щоб перевірити)")
splited_radok = radok.split(" ")
splited_radok[0], splited_radok[-1] = splited_radok[-1], splited_radok[0]
radok = " ".join(splited_radok)
print(radok)