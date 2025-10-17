# Task1
print("Task1")
n = int(input("Vvedit kilkist elementiv masivu"))
while(n < 0):
    n = int(input("Vvedit korektne znachenya (n >= 0)"))
F = []

if (n >= 2):
    F.append(0)
    F.append(1)
    for i in range(2, n):
        F.append(F[-1] + F[-2])
else:
    for i in range(n):
        F.append(n)

print("Vidpovid")
print(F)

# Task2
print("Task2")
n = 7
a = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n-i):
        a[i][j] = j+i+1

for i in range(n):
    print()
    for j in range(n):
        print(a[i][j], end = " ")


# Task3
print("Task3")

a = []

while(True):
    el = input("Vvedit noviy element masivu, vvedit STOP yakcho kinez ")
    if el == "STOP":
        break
    else:
        a.append(el)

print(a)

def vstavka(a, findEl, vstavEl):
    A = list(a)
    if (findEl in A):
        ind = A.index(findEl)
    else:
        print("Takogo elementu ne mae v spisku ")
        return
    A.insert(ind + 1, vstavEl)
    return A


findedEl = input("Vvedit element pisla yakogo vstaviti ")
vstavkaEl = input("Vvedit element yakiy vstavit ")
a = vstavka(a, findedEl, vstavkaEl)
print(a)

#Task4
print("Task 4")

def QuickSort(array):
    spis = list(array)
    if (len(spis) <= 1):
        return spis
    el = spis[-1]
    spis.remove(el)
    left = list(a for a in spis if a <= el)
    right = list(a for a in spis if a > el)
    return QuickSort(left) + [el] + QuickSort(right)



a = []

while(True):
    el = input("Vvedit noviy element masivu (chislo) , vvedit STOP yakcho kinez ")
    if el == "STOP":
        break
    elif el.isdigit() == False:
        print("Vvedeno ne chislo, povtori")
    else:
        a.append(int(el))

a = QuickSort(a)
print("a",a)

#Task5
print("Task 5")

def CompareWithFabiochi(A):
    F = []
    F.append(0)
    F.append(1)
    for i in range(2, 20):
        F.append(F[-1] + F[-2])

    Fabiochi = {f for f in F}
    C = {a for a in A if a in Fabiochi}
    print(f"Fabiochi: {Fabiochi}")
    print(f"A: {A}")
    print(f"Spivpadinnya: {C}")
    return C

MnZilih = {i for i in range(1, 51)}

resMn = CompareWithFabiochi(MnZilih)
print("Vidpovid: ", len(resMn))

