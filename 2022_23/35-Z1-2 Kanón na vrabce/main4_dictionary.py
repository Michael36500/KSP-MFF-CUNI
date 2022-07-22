# import
# from tqdm import tqdm
# import sys

# načtu vstupní soubor
inputf = "2022_23/35-Z1-2 Kanón na vrabce/01.in"
file = open(inputf, "r")

# najdu velikost zahrady a najdu kolik kanónů
print("zahrada")
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
print("read pole")
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

print(kanony)

def checkni_diagonaly(kanon):
    temp = x + kanon[1] - kanon[0]
    return temp

def checkni_diagonaly_naopak(kanon):
    temp = x + kanon[0] - kanon[1]
    return temp

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
for kanon in kanony:
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

print(wasd)

# for kanon in kanony:
#     poradi = checkni_diagonaly_naopak(kanon)
#     docasna = wdas[poradi]
#     docasna.append(kanon[0])
#     wdas[poradi] = docasna
# print("sort")
# for dia in tqdm(range(len(wasd))):
#     temp = wasd[dia]
#     if temp == []:
#         continue
#     temp.sort()

# print("find answer")
# escribo = open("2022_23/35-Z1-2 Kanón na vrabce/out.txt", "w")
# for dia in wasd:
#     if len(dia) > 1:
#         break
# if len(dia) < 2:
#     print("faking nothing")
#     exit()

# indx = wasd.index(dia)

# k_uno_y = indx - x + dia[0]
# k_dos_y = indx - x + dia[1]

# k_uno = []
# k_uno.append(dia[0])
# k_uno.append(k_uno_y)

# # print(indx, x, len(dia), k_uno_y)
# # print(wasd)

# k_dos = []
# k_dos.append(dia[1])
# k_dos.append(k_dos_y)

# escribo = open("2022_23/35-Z1-2 Kanón na vrabce/out.txt", "w")

# escribo.write(str(kanony.index(k_uno)))
# escribo.write(" ")
# escribo.write(str(kanony.index(k_dos)))

# print(str(kanony.index(k_uno)), end = " ")
# print(str(kanony.index(k_dos)))



# # print(wasd)
# # print(wdas)