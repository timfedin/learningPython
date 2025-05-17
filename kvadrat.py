while True: 
    quest = input("Возводим в степень? (Y or N): ").title()
    if quest == "Y" or quest == "Yes" or quest == "No" or quest == "N":
        break
    else:
        print("нераспознано, введите yes или no (или y и n)")
while quest == 'Yes' or quest == 'Y':
    x = input("введите (q для выхода): ")
    if x == "q":
        break
    print(int(x)*int(x))
else:
    print("ну нет так нет, еблан")
print("окончено")
input()