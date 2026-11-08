class Item:
    def __init__(self, litera, size, score):
        self.litera = litera
        self.size = size
        self.score = score


ROWS = int(input("строки:"))
COLS = int(input("столбцы:"))
START = 20
CAPACITY = ROWS * COLS

items = [
    Item('r', 3, 25), Item('p', 2, 15), Item('a', 2, 15), Item('m', 2, 20),
    Item('i', 1, 5),  Item('k', 1, 15), Item('x', 3, 20), Item('t', 1, 25),
    Item('f', 1, 15), Item('d', 1, 10), Item('s', 2, 20), Item('c', 2, 20),
]
all_score = sum(item.score for item in items)

rest = [item for item in items if item.litera != 'd']

good = []

for mask in range(2 ** len(rest)):
    taken = [Item('d', 1, 10)]                       
    for i in range(len(rest)):
        if mask >> i & 1:                
            taken.append(rest[i])

    if sum(item.size for item in taken) > CAPACITY:
        continue                         

    taken_score = sum(item.score for item in taken)
    score = START + taken_score - (all_score - taken_score)

    if score > 0:
        good.append((score, taken))


if len(good) == 0:
    print('Решения нет')
else:
    best_score, best_taken = max(good, key=lambda x: x[0])

    cells = []
    for item in best_taken:
        cells += [item.litera] * item.size
    cells += [' '] * (CAPACITY - len(cells))

    for r in range(ROWS):
        print(','.join('[' + c + ']' for c in cells[r * COLS:(r + 1) * COLS]))
    print('Итоговые очки выживания:', best_score)
    print('Всего комбинаций со счётом > 0:', len(good))
# Доп задание
    file = open('pos_backpacks.txt','w')
    for i in good:
        for j in i[1]:
            file.write(str(f'[{j.litera}] '))
        file.write('\n')
file.close()