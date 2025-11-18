import pandas as pd
import string
import os
import csv
import matplotlib.pyplot as plt
import nltk

#Task1
print("""
-------------------------------------------------------------------------------------
Завдання 1
-------------------------------------------------------------------------------------""")

def ToInt(a):
    a = str(a)
    a = a.replace(".", "")
    a = a.replace("$", "")
    return int(a)

teams = {
  "Teams":["Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9", "Pasha"],
  "Scores":[4, 5, 7 ,8 , 9, 10, 12, 13, 16, 11],
  "Country":["Ukraine", "Germany", "Italy", "USA", "Germany", "USA", "Germany", "Italy", "France", "Ukraine"],
  "Total Income":["20.000$", "30.000$", "50.000$", "60.000$", "60.000$", "80.000$", "75.000$", "120.000$", "200.000$", "100.000$"],
  "Partners Count": [2, 3, 5, 4, 8, 2, 8, 7, 8, 5]
}

colNames = ["Team", "Score", "Country", "Income"]
teamsDf = pd.DataFrame(teams)


print("""
-------------------------------------------------------------------------------------
Аналіз даних
-------------------------------------------------------------------------------------""")
print(teamsDf.head(3))
print(teamsDf.dtypes)
print(teamsDf.shape)
print(teamsDf.describe())



print("""
-------------------------------------------------------------------------------------
Додавання нового стовпця (Дохід від одного партнеру в середньому)
-------------------------------------------------------------------------------------""")
teamsDf["Income from 1 partner (Average)"] = list(map(ToInt, teamsDf["Total Income"]))/teamsDf["Partners Count"]
print(teamsDf)



print("""
-------------------------------------------------------------------------------------
Фільтрація за набраними очками (більше або дорівнює 10)
-------------------------------------------------------------------------------------""")
teamsDf_filtered = teamsDf[teamsDf["Scores"] >= 10]
print(teamsDf_filtered)



print("""
-------------------------------------------------------------------------------------
Сортування за середнім доходом команди від одного партнера (За спаданням)
-------------------------------------------------------------------------------------""")
teamsDf_sorted = teamsDf.sort_values("Income from 1 partner (Average)", ascending=False)
print(teamsDf_sorted)



print("""
-------------------------------------------------------------------------------------
Групування за країнаю та пошук середньої кількості партнерів
-------------------------------------------------------------------------------------""")
teamsDf_grouped = teamsDf.groupby("Country")["Partners Count"].mean().astype(int)
print(teamsDf_grouped)



print("""
-------------------------------------------------------------------------------------
Агрегація
-------------------------------------------------------------------------------------""")
teamsDf["Total_Income"] = teamsDf["Total Income"].apply(ToInt)
print(teamsDf.groupby("Country")["Total_Income"].agg(["sum", "mean", "max"]))



#Task2
print("""
-------------------------------------------------------------------------------------
Завдання 2
-------------------------------------------------------------------------------------""")

fileName = 'comptagevelo2009.csv'

def MakePath(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, file_name)

try:
    df = pd.read_csv(MakePath(fileName), parse_dates=["Date"], dayfirst=True)
except:
    print(f"Не вдалося відкрити файл {fileName}, можливо його не існує")
    exit()


print("""
-------------------------------------------------------------------------------------
Основні характеристики датафрейму
-------------------------------------------------------------------------------------""")
print(df.head())
print(df.info())
print(df.describe())


print("""
-------------------------------------------------------------------------------------
Покращення датафрейму
-------------------------------------------------------------------------------------""")
df = df.fillna(0)
df["Brébeuf"] = df["Brébeuf"].astype(int)
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
df = df.rename(columns={'Unnamed: 1': 'Time'})
pd.set_option('display.max_rows', 10)    #Щоб керувати максимальною кількістю рядків, що виводиться та не скорочується
print(df)

print("""
-------------------------------------------------------------------------------------
Загальна сума всіх велосипедистів
-------------------------------------------------------------------------------------""")
sums = []
names = df.columns.tolist()
names.remove('Date')
names.remove('Time')
for name in names:
     sums.append(sum(df[name]))
print("На всіх велодоріжках за рік: ", sum(sums))
for i in range(len(names)):
      print(f"На дорожці {names[i]}  за рік: {sums[i]}")



print("""
-------------------------------------------------------------------------------------
Найпопулярніші місяці велосипедистів на кожній з 3х обраних велодоріжок
-------------------------------------------------------------------------------------""")

allVariants = names.copy()
chosenVariants = []
while(len(chosenVariants) < 3):
    for i in range(len(chosenVariants), 3):
      print(f"Обери доріжку номер {i+1}")
      for j in range(len(allVariants)):
            print(f"{j} - {allVariants[j]}")
      try:
            chosen = int(input("Введи номер бажаної доріжки "))
            while(chosen < 0 or chosen >= len(allVariants)):
                  chosen = int(input("Введи номер бажаної доріжки (один з наведених вище) "))
            chosenVariants.append(allVariants[chosen])
            allVariants.pop(chosen)
      except:
            print("Невірно введений номер")
            break
    

for i in range(len(chosenVariants)):
      mont = df.resample("ME", on="Date")[chosenVariants[i]].sum()
      print(f"Для доріжки {chosenVariants[i]} найпопулярніший місяць - {mont.idxmax().strftime('%B')}, а саме {max(mont)} користувачів")



print("""
-------------------------------------------------------------------------------------
Графік залежності однієї з велодоріжок по місяцям
-------------------------------------------------------------------------------------""")

for i in range(len(names)):
     print(f"{i} - {names[i]}")

while(True):
     try:
          chosen = int(input("Введіть велодоріжку за якою хочете побачити графік "))
          if (chosen >= 0 and chosen < len(names)):
               break
     except:
          print("Введіть число")



plt.style.use("ggplot")
df.plot(x="Date", y=names[chosen], figsize=(15, 10))
plt.title("Кількість користувачів велодоріжки в різні місяці")
plt.xlabel("Місяці")
plt.ylabel("Кількість користувачів велодоріжки")
plt.show()



#Task3
print("""
-------------------------------------------------------------------------------------
Завдання 3
-------------------------------------------------------------------------------------""")
bookName = "austen-emma.txt"
try:
     with open(MakePath(bookName), 'r') as bookFile:
          text = bookFile.read()
except:
     print(f"Не вдалося відкрити {bookName}, можливо його не існує")



print("""
-------------------------------------------------------------------------------------
Загальлна кількість слів у тексті(до обробки тексту)
-------------------------------------------------------------------------------------""")
words = nltk.tokenize.word_tokenize(text)
print(f"Кількість слів = {len(words)}")



print("""
-------------------------------------------------------------------------------------
10 найпопулярніших слів у тексті (до обробки тексту)
-------------------------------------------------------------------------------------""")
freqDist = nltk.probability.FreqDist(words)
popular = freqDist.most_common(10)
popWord = []
popWordCoun = []
for i in range(len(popular)):
     popWord.append(popular[i][0])
     popWordCoun.append(popular[i][1])
     print(f"{i+1} - Слово '{popWord[i]}' вживається {popWordCoun[i]} раз(ів)")



print("""
-------------------------------------------------------------------------------------
Побудова діаграми...
-------------------------------------------------------------------------------------""")
plt.bar(popWord, popWordCoun)
plt.xlabel("Слова")
plt.ylabel("Кількість слів в тексті")
plt.title("10 найпопулярніших слів у тексті (до обробки тексту)")
plt.show()



print("""
-------------------------------------------------------------------------------------
Загальлна кількість слів у тексті(після обробки тексту)
-------------------------------------------------------------------------------------""")
stopWords = set(nltk.corpus.stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopWords]
print(f"Кількість слів = {len(filtered_words)}")



print("""
-------------------------------------------------------------------------------------
10 найпопулярніших слів у тексті (після обробки тексту)
-------------------------------------------------------------------------------------""")
freqDist = nltk.probability.FreqDist(filtered_words)
popular = freqDist.most_common(10)
popWord = []
popWordCoun = []
for i in range(len(popular)):
     popWord.append(popular[i][0])
     popWordCoun.append(popular[i][1])
     print(f"{i+1} - Слово '{popWord[i]}' вживається {popWordCoun[i]} раз(ів)")



print("""
-------------------------------------------------------------------------------------
Побудова діаграми...
-------------------------------------------------------------------------------------""")
plt.bar(popWord, popWordCoun)
plt.xlabel("Слова")
plt.ylabel("Кількість слів в тексті")
plt.title("10 найпопулярніших слів у тексті (після обробки тексту)")
plt.show()










