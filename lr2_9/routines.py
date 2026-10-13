from csv import reader
from datetime import datetime
import os
import xml.dom.minidom as minidom


def open_table(target):
    try:
        with open(target, 'r') as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table
    except FileNotFoundError:
        print('Файл не найден!')
        return 0


def search(table):
    searchline = input('Введите шаблон поиска: ')
    if searchline in ['0', '']:
        return 0
    elif searchline.isalpha() == False:
        return 0
    flag = 0

    for row in table:
        if (find_string(searchline, row[2]) != -1) and float(row[6].replace(',','.')) >= 200:
            print(row[2])
            flag += 1

    if flag == 0:
        print('Ничего не найдено!')
    else:
        print(f'Найдено позиций: {flag}')
    #input('Нажмите Enter')
    #output.close()


def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index

def xmlread(target):

    xml_file = open(target, 'r')
    xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')
    NumCode, CharCode = [],[]

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        CharCode.append(child.firstChild.data)
                if child.tagName == 'NumCode':
                    if child.firstChild.nodeType == 3:
                        NumCode.append(int((child.firstChild.data)))
    print("CharCode:")
    for c in CharCode:
        print(c,end=' ')
    print()
    print("NumCode:")
    for n in NumCode:
        print(n,end=' ')
    xml_file.close()