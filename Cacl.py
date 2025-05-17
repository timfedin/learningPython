def calcei(argument1, argument2, deistvie):
    if deistvie == '+':
        print('ответ: ', (argument1 + argument2))
    if deistvie == '-':
        print('ответ: ', argument1 - argument2)
    if deistvie == '*':
        print('ответ: ', argument1 * argument2)
    if deistvie == '**':
        print('ответ: ', argument1 ** argument2)
        
a = int(input("1 число: "))
b = int(input("2 число: "))
c = str(input("действие: "))
calcei(a, b, c)
input()