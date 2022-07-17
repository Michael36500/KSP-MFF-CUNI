# importy
from tqdm import tqdm
import numpy as np

# nastavení velikosti zahrady
x = 6 #výška
y = 6  #šířka

# generuju pole polí o velikosti zahrady
zahrada = np.zeros((x, y))
zahrada -= 1

# import pole s pozicemi kanónů
kanony = [[1, 2], [4, 5], [2, 3], [4, 3]]

# loop co dává kanóny do pole / zahrady
for lpnb in range(len(kanony)):

    # do A a B loadnu pozici kanónu
    a = kanony [lpnb] [1]
    b = kanony [lpnb] [0]

    # na dané pozice umístím kanón
    zahrada[a][b] = lpnb


out = []
# loop checkující jestli na úhlopříčce není už nějakej
for lpnb in range(len(kanony)):
    # print(zahrada)
    # získám X a Y kanónu
    kanon = kanony[lpnb]
    
    # najdu začáteční Y pozici (přes X se loopuju)
    # print(start_y)
    start_y = kanon[1] - kanon[0]
    act_y = start_y
    # loop pro jednu úhlopříčku
    # range x === loop přes jednotlivé sloupce
    # print()
    closest_before = None
    closest_after = None
    after_thisone = False
    tempup = []


    
    for sloupec in range(x):
        temp = []
        if act_y < 0 or act_y >= x: #idk it just works
            pass
        else:
            if zahrada[act_y, sloupec] != -1:
                tryit = True
                # print(act_y, sloupec)
                # print(zahrada[act_y, sloupec])
                if zahrada[act_y, sloupec] == lpnb:
                    after_thisone = True
                    tryit = False
                if tryit:
                    if not after_thisone: # means when you are before canon that you are checking
                        closest_before = int(zahrada[act_y, sloupec])

                    if after_thisone: # means when you are after canon that you are checking
                        closest_after = int(zahrada[act_y, sloupec])
                        continue
                    
                        # print(zahrada[act_y, sloupec])

        temp.append(closest_before)
        temp.append(closest_after)

        act_y += 1

    out.append(temp)


out_nao = []
# loop checkující jestli na úhlopříčce není už nějakej
for lpnb in range(len(kanony)):
    # print(zahrada)
    # získám X a Y kanónu
    kanon = kanony[lpnb]
    
    # najdu začáteční Y pozici (přes X se loopuju)
    # print(start_y)
    start_y = kanon[1] + kanon[0]
    act_y_nao = start_y
    # loop pro jednu úhlopříčku
    # range x === loop přes jednotlivé sloupce
    # print()
    closest_before = None
    closest_after = None
    after_thisone = False
    tempup = []


    
    for sloupec in range(x):
        temp = []
        if act_y_nao < 0 or act_y_nao >= x: #idk it just works
            pass
        else:
            if zahrada[act_y_nao, sloupec] != -1:
                tryit = True
                # print(act_y_nao, sloupec)
                # print(zahrada[act_y_nao, sloupec])
                if zahrada[act_y_nao, sloupec] == lpnb:
                    after_thisone = True
                    tryit = False
                if tryit:
                    if not after_thisone: # means when you are before canon that you are checking
                        closest_before = int(zahrada[act_y_nao, sloupec])

                    if after_thisone: # means when you are after canon that you are checking
                        closest_after = int(zahrada[act_y_nao, sloupec])
                        continue
                    
                        # print(zahrada[act_y_nao, sloupec])

        temp.append(closest_before)
        temp.append(closest_after)

        act_y_nao += 1

    out_nao.append(temp)



print(zahrada)
print(out)
print(out_nao)

for a in range(len(out)):
    if out[a, 0] != None:
