import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import string


#Task1
print("Task 1")
x = np.linspace(-2, 5, 100)
y = x * np.sin(5*x)

plt.plot(x,y, label = "x * sin(5x)", color = "blue", linewidth = "5")
plt.title("Task 1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


#Task2

data_file = 'data.csv'
base_dir = os.path.dirname(os.path.abspath(__file__))

def MakePath(nameOfFile):
    return os.path.join(base_dir, nameOfFile)

def ToFloat(a):
    try:
        return float(a)
    except:
        return 0
try:
    with open(MakePath(data_file), 'r') as dataFile:
        reader = csv.DictReader(dataFile, delimiter=',')
        values = []
        for item in reader:
            if (item['Country Name'] == ''):
                del item
            else:
                keys = list(item.keys())[4:-1]
                keys = [key[:4] for key in keys]
                value = list(item.values())[4:-1]
                value = [ToFloat(val) for val in value]
                values.append(value)
                print(item)
except:
    print(f"Не вдалося відкрити файл {data_file}, можливо його не існує")
    exit()


plt.plot(keys, values[0], color = 'red', label = "Ukraine")
plt.plot(keys, values[1], color = 'blue', label = "China")
plt.xlabel("Year")
plt.ylabel("% of population")
plt.title("Access to electricity")
plt.legend()
plt.show()

while(True):
    index = int(input("""
Введіть індекс для країни, відносно якої хочете побачити стовпчасту діаграму
0 - Україна
1 - Китай
    """))
    if (index == 0 or index == 1):
        print("Вибір зафіксовано")
        break
    else:
        print("Такого індексу немає в списку")

plt.bar(keys, values[index])
plt.title("Україна" if index == 0 else "Китай")
plt.show()


#Task3
data = {
  "Team1": 4,
  "Team2": 5,
  "Team3": 7,
  "Team4": 8,
  "Team5": 9,
  "Team6": 10,
  "Team7": 12,
  "Team8": 13,
  "Team9": 16,
  "pasha": 11
}

teams = list(data.keys())
scores = list(map(float, data.values()))

per = []
def Text(x, data):
    score = int((x * sum(data)) / 100)
    per.append(x)
    return f"{x:.1f}% \n {score} points"


wedges, texts, autotexts = plt.pie(scores, autopct= lambda x: Text(x, scores), radius= 1.5)
plt.legend(
    wedges, teams,
    title = "Teams",
    loc = "center right",
    bbox_to_anchor  = (1.3, 0.5, 0, 0)
)

plt.setp(autotexts, size = 8, weight = 'bold')
plt.title("Teams and their scores")
plt.show()