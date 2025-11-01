import os
import string

file1Name = 'TF1_1.txt'
file2Name = 'TF1_2.txt'

#Цей кусочок я піддивився у ШІ і трішки модернізував
#Це потрібно для того щоб файли створювались і шукались в папці, де знаходиться пайтон файл
#Бо так зручніше
base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(yourFileName):
    return os.path.join(base_dir, yourFileName)

file1 = open(MakePath(file1Name), 'w')
text = []
while(True):
    word = str(input("Введіть слово, якщо хочете зупинитись введіть STOP: "))
    if (word == "STOP"):
        break
    else:
        text.append(word)
file1.write(", ".join(text))
file1.close()


try:
    file1 = open(MakePath(file1Name), 'r')
except:
    print("nema")
file2 = open(MakePath(file2Name), 'w')
words = file1.read().split(", ")
file1.close()
for el in words:
    file2.write(el + '\n')
file2.close()

file2 = open(MakePath(file2Name), 'r')
for el in file2:
    print(el, end="")
file2.close()
