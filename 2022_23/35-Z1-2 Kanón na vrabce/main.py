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

for lpnb in range(len(kanony)):

    # a) do A B dám čís. kanónu, jedu úhlopříčky
    a = kanony [lpnb] [1]
    b = kanony [lpnb] [0]

    # print(a, b)
    zahrada[a][b] = lpnb

# zahrada = np.flip(zahrada, 0)
# print(zahrada)

for lpnb in range(len(kanony)):
    kanon = kanony[lpnb]
    print(kanon)
    start_y = kanon[1] - kanon[0]
    print(start_y)
    for a in range(x):
        if a < 0:
            continue
        

