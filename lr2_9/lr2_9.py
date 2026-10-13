import time
from routines import *
table = open_table('books-en.csv')
print("Нажмите любую клавишу...")
while True:
    input()
    os.system('cls')
    if table == 0:
        break
    print('Меню:\n1 - Пункт\n2 - Пункт\n3 - Пункт\n4 - Пункт\n0 - Выход')
    menu = input('Выберите пункт задания: ')
    n = 0
    match menu:
        case '0':
            break
        case '1':
            for row in table:
                n += len(row[1]) > 30
            print(n)
        case '2':
            search(table)
        case '3':
            n = 0
            output = open('result.txt', 'w')
            for row in table[:20]:
                n += 1
                output.write(f'{n}:{row[2]}. {row[1]} - {row[3]}\n')
            output.close()
        case '4':
            xmlread('currency.xml')
        case _:
            print('Нет пункта меню, нажмите Enter')
            input()
