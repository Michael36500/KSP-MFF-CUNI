# importy
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

# loop checkující jestli na úhlopříčce není už nějakej, potřeba dodělat
for lpnb in range(len(kanony)):
    # print(zahrada)
    # získám X a Y kanónu
    kanon = kanony[lpnb]
    
    # najdu začáteční Y pozici (přes X se loopuju)
    start_y = kanon[1] - kanon[0]
    # print(start_y)
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
                # print(act_y, sloupec)
                # print(zahrada[act_y, sloupec])
                if zahrada[act_y, sloupec] == lpnb:
                    after_thisone = True
                    continue

                if not after_thisone: # means when you are before canon that you are checking
                    closest_before = zahrada[act_y, sloupec]

                if after_thisone: # means when you are after canon that you are checking
                    closest_after = zahrada[act_y, sloupec]

        temp.append(closest_before)
        temp.append(closest_after)
        temp.append(lpnb)


        act_y += 1
    out.append(temp)
    # break
print(zahrada)
print(out)