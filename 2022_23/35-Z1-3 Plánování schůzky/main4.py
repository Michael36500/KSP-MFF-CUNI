# import
from tqdm import tqdm   
import numpy as np

# načtu vstupní soubor
inputf = "2022_23/35-Z1-2 Kanón na vrabce/vstup"
file = open(inputf, "r")

# najdu velikost zahrady a najdu kolik kanónů
line = file.readline()
x_line = ""
for a in line:
    line = line[1:]
    if a == " ":
        break
    x_line = str(x_line) + str(a)
x = int(x_line) #výška

y_line = ""
for a in line:
    line = line[1:]
    if a == " ":
        break
    y_line = str(y_line) + str(a)
y = int(y_line)  #šířka

kolikk = ""
for a in line:
    line = line[1:]
    if a == " ":
        break
    kolikk = str(kolikk) + str(a)
kolik = int(kolikk) 

# print(x, y, kolik)


# import pole s pozicemi kanónů
kanony = []
def read_kanon(lp):
    global file
    global kanony

    line = file.readline()
    x_line = ""
    for a in line:
        line = line[1:]
        if a == " ":
            break
        x_line = str(x_line) + str(a)
    x = int(x_line) #výška

    y_line = ""
    for a in line:
        line = line[1:]
        if a == " ":
            break
        y_line = str(y_line) + str(a)
    y = int(y_line)  #šířka

    temp = []
    temp.append(x)
    temp.append(y)
    # temp.append(lp)

    kanony.append(temp)

for a in range(kolik):
    read_kanon(a)

print(kanony)

def checkni_diagonaly(kanon):
    # print(kanon, end = " ")
    temp = x + kanon[1] - kanon[0]
    # print(temp)
    return temp

wasd = [] # zleva nahoře doprava dolů
wdas = [] # zprava nahoře doleva dolů
empty = []

for _ in range(x + y):
    wasd.append(empty)
    wdas.append(empty)


for kanon in kanony:
    print(wasd)
    poradi = checkni_diagonaly(kanon)
    temp = wasd[poradi]
    temp.append(kanon[0])
    wasd[poradi] = temp


print(wasd)
print(wdas)