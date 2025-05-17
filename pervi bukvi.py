names = str(input('Через запятую с пробелами: '))
names = names.split(', ')
num = 0
first = []
for i in range(len(names)):
    first.append(names[num][0])
    num = num + 1
first = ''.join(first).lower()
print(first)
    
input()
