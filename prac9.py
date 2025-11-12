import csv
import os

#Task 1
print(
    "====================",
    "\nЗавдання 1",
    "\n===================="
)
fileName = 'GDP_per_capita.csv'
base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(nameOfFile):
    return os.path.join(base_dir, nameOfFile)


try:
    csvFile = open(MakePath(fileName), 'r')
    reader = csv.DictReader(csvFile, delimiter = ',')
    print("Весь файл: ")
    for r in reader:
        print(r)
    csvFile.close()
except:
    print(f"Не вдалося відкрити файл {fileName}, можливо його не існує")

try:
    csvFile = open(MakePath(fileName), 'r')
except:
    print(f"Не вдалося відкрити файл {fileName}, можливо його не існує")
reader = csv.DictReader(csvFile, delimiter = ',')
country = str(input("Введіть країну яку хочете знайти: "))
isFounded = False
for r in reader:
    if (r['Country Name'] == country):
        isFounded = True
        answer = r
        print(f"{answer['Country Name']} had {answer['Series Name']} = {answer['2019 [YR2019]']} in 2019 year")
        try:
            with open(MakePath('Resault.csv'), 'w') as res:
                writer = csv.writer(res, dialect = 'excel')
                writer.writerows(answer.items())
        except:
            print(f"Не вдалося записати")
if (isFounded == False):
    print("Такої країни немає в списку")
csvFile.close()





#Task2
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
def MakePath(nameOfFile):
    return os.path.join(base_dir, nameOfFile)

#Функціх
def OutputJSON(json_file_name):
    try:
        with open(MakePath(json_file_name), 'r') as json_file:
            data = json.load(json_file)
    except:
        print(f"Не вдалося відкрити файл {json_file_name}, можливо його не існує")
        exit()
    print("Вивід файлу: ")
    print(data)

def AddToJSON(json_file_name, key, value):
    try:
        with open(MakePath(json_file_name), 'r') as json_file:
            data = json.load(json_file)
    except:
        print(f"Не вдалося відкрити файл {json_file_name}, можливо його не існує")
        exit()
    data[key] = value
    try:
        with open(MakePath(json_file_name), 'w') as json_file:
            json.dump(data, json_file, indent = 2)
    except:
        print("Не вдалося записати")

def DeleteFromJSON(json_file_name, key):
    try:
        with open(MakePath(json_file_name), 'r') as json_file:
            data = json.load(json_file)
    except:
        print(f"Не вдалося відкрити файл {json_file_name}, можливо його не існує")
        exit()
    if (data[key] != None):
        print(f"За ключем {key} видалено {data[key]}")
        del data[key]
        try:
            with open(MakePath(json_file_name), 'w') as json_file:
                json.dump(data, json_file, indent = 2)
        except:
            print("Не вдалося записати")
    else:
        print(f"Ключа {key} не існує в цьому файлі")

def FindDataFromJSON(json_file_name, key):
    try:
        with open(MakePath(json_file_name), 'r') as json_file:
            data = json.load(json_file)
    except:
        print(f"Не вдалося відкрити файл {json_file_name}, можливо його не існує")
        exit()
    print(f"Знайдена інформація за ключем {key} = {data[key]}")

#Загальні завдання
print(
    "====================",
    "\nЗагальні завдання",
    "\n===================="
)
jsonFileName = 'TaskForAllStudents.json'
data = {
    "Name": "Pasha",
    "Age": 18
}
try:
    with open(MakePath(jsonFileName), 'w') as jsonFile:
        json.dump(data, jsonFile, indent=2)
except:
    print("Не вдалося записати")

OutputJSON(jsonFileName)
AddToJSON(jsonFileName, 'Phone Number', '+380 93 829 22 29')
DeleteFromJSON(jsonFileName, 'Age')
FindDataFromJSON(jsonFileName, 'Name')
OutputJSON(jsonFileName)

#Завдання за віріантом
print(
    "====================",
    "\nЗавдання за варіантом",
    "\n===================="
)
team_names = ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9"]
team_scores = [4, 5, 7, 8, 9, 10, 12, 13, 16, 22,]
teams = dict(zip(team_names, team_scores))
print("Список команд")
print(teams)

try:
    myTeamName = str(input("Введіть назву вашої команди: "))
    myTeamScore = int(input("Введіть кількість очок вашої команди: "))
except ValueError:
    print("Некоректний формат")

teams[myTeamName] = myTeamScore

def Sort(teams):
    sorted_teams = dict(sorted(teams.items(), key=lambda x: x[1], reverse=True ))
    print("Список команд з вашою командою")
    print (sorted_teams)
    return sorted_teams

sorted_teams = Sort(teams)

def FindPlace(sorted_teams):
    scores = list(sorted_teams.values())
    place = scores.index(myTeamScore) + 1
    print(f"Ваша команда займає {place} місце!")
    return place

place = FindPlace(sorted_teams)

def FindWorse(teams):
    worse_teams = [key for key, value in teams.items() if value < myTeamScore]
    print("Команди, гірші за вашу: ")
    print(worse_teams)
    return worse_teams

worse_teams = FindWorse(teams)

try:
    with open(MakePath('my_json_file.json'), 'w') as myJSON:
        json.dump(teams, myJSON, indent = 2)
except:
    print("Не вдалося записати")

print("Done")