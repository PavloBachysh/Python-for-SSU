import requests
import datetime
from bs4 import BeautifulSoup
import os
import json

#Виконує запит на сайт і повертає обєкт класу BeautifulSoup
def ChooseForecast(default = False):
    while(True):
        if (default):
            link_name = f"https://sinoptik.ua/pohoda/sumy/{datetime.date.today()}"
            response = requests.get(link_name)
        else:
            city = str(input("Введіть ваше місто (Англайська мова): ")).lower()
            date = BuildDate()
            forecast_date = date
            link_name = f"https://sinoptik.ua/pohoda/{city}/{forecast_date}"
            response = requests.get(link_name)
        if response.ok:
            print("Доступ отримано")
            print(f"Статус {response.status_code}")
            break
        else:
            print("Не вдалося отримати доступ")
            print(f"Код помилки: {response.status_code}")
    soup = BeautifulSoup(response.text, "lxml")
    return soup

#Локальна база даних
def CreateDB(keys, values):
    db = dict(zip(keys, values))
    return db

#Додає інформацію до бази даних
def AddToDB(your_keys, your_values, keys, values):
    if(your_keys not in keys):
        keys.extend(your_keys)
        values.extend(your_values) 
    return keys, values   

#Функція, за допомогою якої створюється дата (за яку користувач буде переглядати прогноз). Існує багато перевірок, щоб дата була коректна
def BuildDate():
    while(True):
        try:
            y = str(input("Введи рік (число формату yyyy): "))
            m = str(input("Введи місяць (число формату mm): "))
            d = str(input("Введи день (число формату dd): "))
            if (len(y) != 4 or len(m) != 2 or len(d) != 2):
                print("Некоректний формат дати, повинен бути рік повинен мати 4 символи, а день та місяць по 2")
                continue
            else:
                date = f"{y}-{m}-{d}"
                term = (datetime.date.fromisoformat(date) - datetime.date.today()).days
                if (term >= 11 or term <= -90):
                    print("Обрана дата повинна бути не більше ніж 89 днів тому та не більше ніж через 9 днів")
                    continue
                else:
                    break
        except:
            print("Неправильна дата")
            continue

    return date

#Виводить головну інформацію
def MainInfo(soup):
    print(f"Заголовок: {Title(soup)}")
    description = soup.find("p", {"class": "GVzzzKDV"})
    forecast = soup.find("a", {"class": "tkK415TH OGO-yOID"}).get("aria-label")
    print(f"Короткий опис: {forecast}")
    print(f"Опис: {description.text}")
    return forecast, description.text
    

#Повертає заголовок сайту
def Title(soup):
    title = soup.title.text
    return title

#Можна розрахувати мінімальне, середнє та максимальне значення за деякими критеріями. (Якщо макс або мінамальне, то демонструється час, коли це було/буде)
def GetMaxOrMinOrMean(soup, mode): # -1 = min, 1 = max, 0 = mean
    while(True):
        match mode:
            case -1:
                print(f"""-----------------------------------------------------------------------
1 - Мінімальна температура за день
2 - Мінімальний атмосферний тиск за день
3 - Мінімальна вологість за день
4 - Мінімальна ймовірність осадків за день
-----------------------------------------------------------------------""")
            case 0:
                print(f"""-----------------------------------------------------------------------
1 - Середня температура за день
2 - Середній атмосферний тиск за день
3 - Середня вологість за день
4 - Середня ймовірність осадків за день
-----------------------------------------------------------------------""")
            case 1:
                print(f"""-----------------------------------------------------------------------
1 - Максимальна температура за день
2 - Максимальний атмосферний тиск за день
3 - Максимальна вологість за день
4 - Максимальна ймовірність осадків за день
-----------------------------------------------------------------------""")
        try:
            choose = int(input("Введи номер бажаної операції: ")) - 1
            if (choose >= 0 and choose <= 3):
                break
            else:
                print("Операції з таким номером не існує")
        except:
            print("Виникла помилка, спробуй ще")

    criteria = {
    "Temperature": 3,
    "Pressure": 5,
    "Water": 6,
    "Prop_Precipitation": 8
}
    crit_val = list(criteria.values())
    idx = crit_val[choose]


    information = soup.find_all("tr", {"class": "qaGibDrT"})
    data = information[idx].find_all("td")

    texts = [
        ["Мінімальна температура за день: ", "Мінімальний атмосферний тиск за день: ", "Мінімальна вологість за день: ", "Мінімальна ймовірність опадів за день: "],
        ["Середня температура за день: ", "Середній атмосферний тиск за день: ", "Середня вологість за день: ", "Середня ймовірність опадів за день: "],
        ["Максимальна температура за день: ", "Максимальний атмосферний тиск за день: ", "Максимальна вологість за день: ", "Максимальна ймовірність опадів за день: "]
        ]
            
    if (idx == 3):
        for i in range(len(data)):
            data[i] = data[i].text
            data[i] = data[i][:-1]
            data[i] = data[i].replace("+", "")
            data[i] = int(data[i])
    else:
        for i in range(len(data)):
            if('-' in data[i].text):
                data[i] = int(data[i].text.replace('-', '0'))
            else:
                data[i] = int(data[i].text)
    match mode:
        case -1:
            res_data = min(data)
            text = texts[0]
        case 0:
            res_data = sum(data)/len(data)
            text = texts[1]
        case 1:
            res_data = max(data)
            text = texts[2]

    print(text[choose], res_data)
    if (mode == 1 or mode == -1):
        time_index = data.index(res_data)
        time = information[1].find_all("td")[time_index].text
        print(f"І це було/буде о: {time}")
    return res_data, text[choose]

#Інформація про години сходу та заходу сонця
def SunSet(soup):
    times = soup.find_all("span", {"class": "WJJwi+RN"})
    texts = ["Схід сонця", "Захід сонця"]
    print(f"{texts[0]}: {times[0].text}, {texts[1]}: {times[1].text}")
    return [times[0].text, times[1].text], texts

#Інформація про рекордні температури цього дня місяця
def Record(soup):
    texts = ["Рекордно максимальна температура", "Рекордно мінімальна температура"]
    try:
        times = soup.find_all("span", {"class": "objEyGOn"})
        print("Рекорд")
        print(f"Максимальна температура: {times[0].text}, Мінімальна температура: {times[1].text}")
        times = [times[0].text, times[1].text]
    except:
        times = ["Немає даних про рекорд в цей день в цьому міті", "Немає даних про рекорд в цей день в цьому міті"]
        print(times)
    return times, texts

#Зберігає все в файл
def SaveInFile(db):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'forecast.json'
    dir = os.path.join(base_dir, file_name)
    try:
        with open(dir, 'w') as json_file:
            json.dump(db, json_file, ensure_ascii=False, indent=2)
    except:
        print("Не вдалося створити файл")
    print(f"Дані збережено у файл під назвою '{file_name}'")
    


#Текст головного меню
def PrintMainMenu(soup):
    print(f"""
======================================================================================================================
{Title(soup)}
1 - Змінити місто та день
2 - Вивести головну інформацію
3 - Мінімальні значення за день
4 - Середні значення за день
5 - Максимальні значення за день
6 - Рекорд у цей день
7 - Час сходу і заходу сонця
8 - Зберегти виведені значення до файлу
0 - Закінчити роботу з програмою
======================================================================================================================
""")

#Спочатку використовує стандартні значення (м. Суми, день - сьогодні) і виводить головні відомості
soup = ChooseForecast(True)
keys = []
values = []

#Основний функціонал програми
while(True):
    PrintMainMenu(soup)
    try:
        choose = int(input("Введи номер бажаної операції: "))
        print("----------------------------------------------------------------")
    except:
        print("Виникла помилка, спробуй ще")
        continue
    match choose:
        case 1:
            soup = ChooseForecast()
            keys = []
            values = []
        case 2:
            short_des, des = MainInfo(soup)
            names = ["Заголовок", "Короткий опис", "Опис"]
            vals = [Title(soup), short_des, des]
            AddToDB(names, vals, keys, values)
        case 3:
            res_dat, res_text = GetMaxOrMinOrMean(soup, -1)
            names = [res_text]
            vals = [res_dat]
            AddToDB(names, vals, keys, values)
        case 4:
            res_dat, res_text = GetMaxOrMinOrMean(soup, 0)
            names = [res_text]
            vals = [res_dat]
            AddToDB(names, vals, keys, values)
        case 5:
            res_dat, res_text = GetMaxOrMinOrMean(soup, 1)
            names = [res_text]
            vals = [res_dat]
            AddToDB(names, vals, keys, values)
        case 6:
            res_dat, res_text = Record(soup)
            names = res_text
            vals = res_dat
            AddToDB(names, vals, keys, values)
        case 7:
            res_dat, res_text = SunSet(soup)
            names = res_text
            vals = res_dat
            AddToDB(names, vals, keys, values)

        case 8:
            SaveInFile(local_db)
        case 0:
            print("Закінчую...")
            break
    local_db = CreateDB(keys, values)
            
