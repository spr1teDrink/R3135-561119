import time, sys, os

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[30m'
ERASE = '\x1B[2K' # erase the line
BEGIN = '\x1B[1G' # return to column 1

#1
'''
pixel = ' '
scale = 1
chunk = pixel*scale*5
def line(pattern):
    for i in range(scale*2):
        print(pattern)

line(WHITE + chunk + BLUE + chunk + WHITE + chunk*2 + END)
line(BLUE + chunk + BLUE + chunk + BLUE + chunk*2 + END)
line(WHITE + chunk + BLUE + chunk + WHITE + chunk*2 + END)

#2
def draw_line(strch,radius,y):
    for x in range(-radius*strch[0],(radius+1)*strch[0]-1):
        if ((x/strch[0])**2 + (y*strch[1])**2) <= radius**2:
            print(BLACK + ' ' + END,end='')
        else:
            print(WHITE + ' ' + END,end='')
            
def circle(radius):
    strch = 2,1.1
    for y in range(radius+1,-(radius+1),-1):
        draw_line(strch,radius,y)
        draw_line(strch,radius,y)
        print()
circle(6)

#3
frames = '|','/','—','\\'
i = 0
while True:
    os.system("cls")
    print(frames[i])
    time.sleep(1)
    i += 1
    i %= 4

#4 Не совсем понял 
file = open('sequence.txt','r')
neg = []
pos = []
for i in file:
    n = float(i)
    if -5 >= n > -10:
        neg.append(n)
    elif 5 <= n < 10:
        pos.append(n)
negl = len(neg)
posl = len(pos)
sum = negl + posl
print(f"{RED}{' '*int(negl)}{END}|{negl*100/sum}%")
print(f"{BLUE}{' '*int(posl)}{END}|{posl*100/sum}%")
'''
