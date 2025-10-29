mySlownyk = {
    "Паша": 15,
    "Misha": 7,
    "Dasha": 13,
    "Маша": 4,
    "Світлана": 16
}


def VivestiZnachennya(slownyk):
    for key, value in slownyk.items():
        print(key, ": ", value)

def DodatiElement(key, value, slownyk):
    slownyk[key] = value
    return slownyk

def VidalityElement(key, slownyk):
    if key in slownyk:
        del slownyk[key]
    else:
        print(f"Такого елемненту немає в словнику ({key})")
    return slownyk

def SortSlownyk(slownyk):
    listt = list(slownyk)
    listt.sort()
    print("Відсортовано")
    for el in listt:
        print(f"{el}: {slownyk[el]}")

while (True):
    print(
        "1 - Вивести словник\n",
        "2 - Вивести словник відсортований за алфавітом\n",
        "3 - Додати елемент у словник\n",
        "4 - Видалити елемент з словника\n",
        "5 - Завершити роботу з словником",
    )
    func = int(input("Оберіть номер дії, описаних вище: "))

    match func:
        case 1:
            VivestiZnachennya(mySlownyk)
        case 2:
            SortSlownyk(mySlownyk)
        case 3:
            try:
                choose = 1
                key = str(input("Введіть імя: "))
                val = int(input("Введіть к-сть придбаних жетонів : "))
            except ValueError:
                print("Некоректний формат")
            if key in mySlownyk:
                print("Таке імя вже є в словнику")
                print(
                    "1 - Змінити значення",
                    "\n2 - Проігнорувати"
                )
                while(True):
                    try:
                        choose = int(input("Введіть номер дії : "))
                        break
                    except:
                        print("Некоректний формат")
                        continue
            if (choose == 1):
                DodatiElement(key, val, mySlownyk)
            
        case 4:
            toDel = str(input("Введіть імя для видалення з словнику: "))
            if toDel not in mySlownyk:
                print("Таке імя нема в словнику")
            VidalityElement(toDel, mySlownyk)
        case 5:
            print("Завершую...")
            break


#Команди

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




