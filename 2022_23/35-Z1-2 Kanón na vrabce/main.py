# importy
import numpy as np

# nastavení velikosti zahrady
y = 6  #šířka
x = 6 #výška

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

# loop checkující jestli na úhlopříčce není už nějakej, potřeba dodělat
for lpnb in range(len(kanony)):
    # získám X a Y kanónu
    kanon = kanony[lpnb]
    print(kanon)
    
    # najdu začáteční Y pozici (přes X se loopuju)
    start_y = kanon[1] - kanon[0]
    print(start_y)

    # loop pro jednu úhlopříčku
    for a in range(x):
        if a < 0:
            continue
        

