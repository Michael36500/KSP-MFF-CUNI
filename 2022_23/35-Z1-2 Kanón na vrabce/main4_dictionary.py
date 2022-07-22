# import
from tqdm import tqdm
# import sys

# načtu vstupní soubor
inputf = "2022_23/35-Z1-2 Kanón na vrabce/05.in"
file = open(inputf, "r")

# najdu velikost zahrady a najdu kolik kanónů
# print("zahrada")
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

# # print(x, y, kolik)


# import pole s pozicemi kanónů
# print("read pole")
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

    kanontmp = []
    kanontmp.append(x)
    kanontmp.append(y)
    # kanontmp.append(lp)

    kanony.append(kanontmp) 

for a in range(kolik):
    read_kanon()

# print(kanony)

def checkni_diagonaly(kanon):
    temp = x + kanon[1] - kanon[0]
    return temp

# def checkni_diagonaly_naopak(kanon):
#     temp = x + kanon[0] - kanon[1]
#     return temp

# wasd = [] # zleva nahoře doprava dolů
# wdas = [] # zprava nahoře doleva dolů

print("make pole")
# wasd = [[]] * (x + y)# zleva nahoře doprava dolů
wasd = {}
# wdas = [[]] * (x + y)# zprava nahoře doleva dolů
# wasd *= 1
# wdas *= 1
# print(sys.getsizeof(wasd))
# wasd = [] # zleva nahoře doprava dolů
# wdas = [] # zprava nahoře doleva dolů

# for _ in tqdm(range(x + y)):
#     empty = []
#     wasd.append(empty)
#     empty = []
#     wdas.append(empty)


# print(wasd)
# print(wdas)
print("check diagonaly")
for kanon in tqdm(kanony):
    poradi = checkni_diagonaly(kanon)
    if poradi in wasd:
        docasna = wasd[poradi]
        # print(docasna)
        docasna.append(kanon[0])
        # wasd[poradi] = docasna # není potřeba
    else:
        empty = []
        empty.append(kanon[0])
        wasd[poradi] = empty
    # if poradi in wasd:
    #     docasna = wasd[poradi]
    #     docasna.append(kanon[0])
    #     wasd[poradi] = docasna
    # else:
    #     wasd.update(poradi = kanon[0])

def runit():
    global kanony
    global wasd
    global x

    for a in wasd:
        temp = wasd[a]
        if len(temp) > 1:
            temp.sort()
            kan_uno = temp[0]
            kan_dos = temp[1]

            kan_uno_y = a + kan_uno - x
            kan_dos_y = a + kan_dos - x

            kan_uno_list = []
            kan_uno_list.append(kan_uno)
            kan_uno_list.append(kan_uno_y)

            kan_dos_list = []
            kan_dos_list.append(kan_dos)
            kan_dos_list.append(kan_dos_y)

            # print(kan_dos_list)
            kan_uno_indx = kanony.index(kan_uno_list)
            kan_dos_indx = kanony.index(kan_dos_list)

            return kan_uno_indx, kan_dos_indx



print("find answer")
escribo = open("2022_23/35-Z1-2 Kanón na vrabce/out.txt", "w")

out_str = str(runit())
out_str = out_str.replace("(", "")
out_str = out_str.replace(")", "")
out_str = out_str.replace(",", "")

print(out_str)

escribo.write(out_str)
