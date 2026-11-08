import re
import csv
#1
file1 = open('task1-en.txt','r').read()

result11 = re.findall(r'\b\w*e\b',file1)
result12 = re.findall(r'\(\d+\)', file1)
#print(result12)
#print(result11)

#2
file2 = open('task2.html', 'r', encoding='utf-8').read()

result2 = re.findall(r'\bsizes="(\d+x\d+)"',file2)
#print(result2)

#3

file3 = open('task3.txt','r').read()

id = re.findall(r' (\d+) ',file3)
surname = re.findall(r' ([A-Za-z]+) ',file3)
email = re.findall(r'\b\w+@[\w-]+\.\w+\b',file3)
date = re.findall(r'\b\d+-\d+-\d+\b',file3)
site = re.findall(r'\bhttps?://[\w\.-]+\b',file3)

result3 = []
with open('result.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\n')

    writer.writerow(['ID', 'Surname', 'Email', 'Date', 'Site'])

    for i in range(len(id)):
        writer.writerow([
            id[i],
            surname[i],
            email[i],
            date[i],
            site[i]
        ])

# Доп задание
file4 = open('task_add.txt','r').read()
email4 = re.findall(r'\w+@[a-z-]+\.[a-zA-Z]+',file4)
date4 = re.findall(r'\d{2,4}[\./-]\d{2}[\./-]\d{2,4}',file4)
site4 = re.findall(r'https?://[a-zA-Z\.-]+',file4)

#print(email4)
#print(date4)
#print(site4)