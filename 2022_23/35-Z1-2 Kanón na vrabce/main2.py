# import
from tqdm import tqdm
import numpy as np

# načtu vstupní soubor
inputf = "2022_23/35-Z1-2 Kanón na vrabce/01.in"
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

print(x, y, kolik)


# import pole s pozicemi kanónů
kanony = []
def read_kanon():
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

    kanony.append(temp)

for _ in range(kolik):
    read_kanon()

print(kanony)


def checkni_diagonaly(a):
    global kanony
    global x
    global y

    print(kanony[a])
    kanon = kanony[a]
    

for a in range(len(kanony)):
    checkni_diagonaly(a)