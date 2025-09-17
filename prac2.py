#Task1
import math
import random
print("Task1")

def funcZ(m,n):
    return (math.sqrt(2) - math.sqrt(3*n))/(2*m) if m != 0 else print("Znamennik = 0")

m = float(input("Vvedi m: "))
n = float(input("Vvedi n: "))

z = funcZ(m,n)
print(z)


print("Komputer zagadav chislo vid 1 do 100, sprobuy vgadati")

targetNum = random.randint(1, 100)
def vgad(userNum):
    while(True):
        if userNum < targetNum:
            userNum = int(input("Chislo komputera bilshe, vvedit inshe znachennya: "))
        elif userNum > targetNum:
            userNum = int(input("Chislo komputera menshe, vvedit inshe znachennya: "))
        else:
            print("Vi vgadaly")
            break

userNum = int(input("Vvedi zile chislo vid 1 do 100: "))
vgad(userNum)

#Task2
print("Task2")
from vgadayka import vgaday

print("Komputer znovu zagadav chislo vid 1 do 100, sprobuy vgadati")
userNum = int(input("Vvedi zile chislo vid 1 do 100: "))
vgaday(userNum)
