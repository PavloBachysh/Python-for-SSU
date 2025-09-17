#Task1
print("Task1")

while(True):
    a = float(input("Vvedit dodatne a"))
    b = float(input("Vvedit dodatne b"))
    if (a >= 0 and b >= 0):
        break

def function(a, b):
    if (a > b):
        return a * b + 1
    elif (a == b):
        return 25
    else:
        return (a-5)/b if b != 0 else 0
    
print(f"Vidpovid {function(a,b)}")

#Task2
print("Task2")

print("Chisla v diapasoni vid 30 do 60, kratni 3")
for i in range(30, 61):
    if (i % 3 == 0):
        print(i)

#Task3
print("Task3")

while(True):
    n = int(input("Vvedit N, yake 1<N<9"))
    if (n > 1 and n < 9):
        break

for i in range(n+1):
    num = n
    for j in range(i):
        print(num, end = " ")
        num -= 1
    print("")