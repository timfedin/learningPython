from datetime import datetime

name = input("имя: ").title()
gender = list(input("гендер: "))

if "м" in gender or gender[0] == "m" in gender:
    gender = "Мужчина"
else:
    gender = "Женщина"
    
date = str(datetime.now().year - int(input("возраст: ")))

human = {
    "имя": name,
    "пол": gender,
    "год рождения": date
}
print(human)
input()