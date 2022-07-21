# import
# from tqdm import tqdm
# import numpy as np

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

    kanontmp = []
    kanontmp.append(x)
    kanontmp.append(y)
    # kanontmp.append(lp)

    kanony.append(kanontmp) 

for a in range(kolik):
    read_kanon(a)

# print(kanony)

def checkni_diagonaly(kanon):
    temp = x + kanon[1] - kanon[0]
    return temp

def checkni_diagonaly_naopak(kanon):
    temp = x + kanon[0] - kanon[1]
    return temp

wasd = [] # zleva nahoře doprava dolů
wdas = [] # zprava nahoře doleva dolů


for _ in range(x + y):
    empty = []
    wasd.append(empty)
    empty = []
    wdas.append(empty)

# wasd = str(wasd)
wasd = list(wasd)

# print(wasd)
# print(wdas)

for kanon in kanony:
    poradi = checkni_diagonaly(kanon)
    docasna = wasd[poradi]
    docasna.append(kanon[0])
    wasd[poradi] = docasna

# for kanon in kanony:
#     poradi = checkni_diagonaly_naopak(kanon)
#     docasna = wdas[poradi]
#     docasna.append(kanon[0])
#     wdas[poradi] = docasna

for dia in range(len(wasd)):
    temp = wasd[dia]
    temp.sort()

escribo = open("2022_23/35-Z1-2 Kanón na vrabce/out.txt", "w")
for dia in wasd:
    if len(dia) > 1:
        # escribo.write(str(dia[0]))
        # escribo.write(" ")
        # escribo.write(str(dia[1]))
        # print(dia[0])
        # print(dia[1])
        break
if len(dia) < 2:
    print("faking nothing")
    exit()

indx = wasd.index(dia)
print(dia, indx)

k_uno_y = indx - x + dia[0]
k_dos_y = indx - x + dia[1]

k_uno = []
k_uno.append(dia[0])
k_uno.append(k_uno_y)

k_dos = []
k_dos.append(dia[1])
k_dos.append(k_dos_y)

kanony.index(k_uno)
kanony.index(k_dos)

print(wasd)
# print(wdas)