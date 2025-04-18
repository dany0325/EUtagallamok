#Ezt tanár úrnak nem kell megnézni, csak megakartam csinálni objektumokkal

#2. feladat
class Country:
    def __init__(self, name, date):
        self.name = name
        self.date = date

countries = list()

with open("EUcsatlakozas.txt", "r", encoding="utf-8") as SOURCE_FILE:
    for i in SOURCE_FILE:
        temp = i.strip().split(";")
        country_temp = Country(temp[0], temp[1])
        countries.append(country_temp)

#3. feladat
eu_before_2018_count = 0

for i in countries:
    if int(i.date[0:4]) < 2018:
        eu_before_2018_count += 1

print(f"3. feladat: 2018-ban {eu_before_2018_count} ország volt az EU része.")

#4. feladat
eu2007_count = 0

for i in countries:
    if "2007" in i.date:
        eu2007_count += 1

print(f"4. feladat: 2007-ben {eu2007_count} ország csatlakozott az EU-hoz.")

#5. feladat
for i in countries:
    if i.name == "Magyarország":
        print(f"5. feladat: Magyarország csatlakozása: {i.date}")
        break

#6. feladat
for i in countries:
    if ".05." in i.date:
        print("6. feladat: Májusban volt csatlakozás")
        break

#7. feladat
last_country = Country("N/A", "0000.00.00")

for i in countries:
    if int(i.date[0:4]) > int(last_country.date[0:4]):
        last_country = i

print(f"7. feladat: Legutolsó csatlakozó ország: {last_country.name}")

#8. feladat
dates = dict()
for i in countries:
    date = i.date[0:4]
    if date in dates:
        dates[date] += 1
    else:
        dates[date] = 1

print("8. feladat: Statisztika: ", dates)