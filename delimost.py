chislo = int(input("Какое число вы хотите проверить на делимость?: "))
min = int(input("В диапозоне от какого числа вы хотите проверить?: "))
max = int(input("В диапозоне до какого числа вы хотите проверить?: "))
delimost = []
for i in range(min, max+1):
    if chislo % i == 0:
        delimost.append(str(i))
print('Делится на ', ', '.join(delimost))
