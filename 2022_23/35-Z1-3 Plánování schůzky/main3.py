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

print(x, y, kolik)


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

kanony_sort = kanony.sort()
print(kanony)


def checkni_diagonaly(a):
    global kanony
    global x
    global y

    print(kanony[a])
    kanon = kanony[a]
    temp = kanon
    while True:
        temp[0] = temp[0] - 1
        temp[1] = temp[1] - 1
        if min(temp) == 0:
            break
    return temp

diagonals = []
for a in range(kolik):
    diagonals.append(checkni_diagonaly(a))

print(diagonals)

duplicates = [number for number in diagonals if diagonals.count(number) > 1]
unique_duplicates = set(duplicates)

print(duplicates, "dups", unique_duplicates, "uniq")

def checkni_diagonaly_sort(a):
    global kanony
    global x
    global y

    print(kanony[a])
    kanon = kanony[a]
    temp = kanon
    while True:
        temp[0] = temp[0] - 1
        temp[1] = temp[1] - 1
        if min(temp) == 0:
            break
    return temp

diagonals_sort = []
for a in range(kolik):
    diagonals_sort.append(checkni_diagonaly_sort(a))

print(diagonals_sort)
