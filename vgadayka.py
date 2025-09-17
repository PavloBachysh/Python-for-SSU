import random
targetNum = random.randint(1, 100)
def vgaday(userNum):
    while(True):
        if userNum < targetNum:
            userNum = int(input("Chislo komputera bilshe, vvedit inshe znachennya: "))
        elif userNum > targetNum:
            userNum = int(input("Chislo komputera menshe, vvedit inshe znachennya: "))
        else:
            print("Vi vgadaly")
            break