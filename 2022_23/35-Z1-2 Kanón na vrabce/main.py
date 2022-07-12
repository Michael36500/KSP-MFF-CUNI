import numpy as np
# 1. array o velikosti zahrady
x = 6
y = 6

zahrada = np.zeros((x, y))
zahrada -= 1
# print(zahrada)

kanony = [[1, 2], [4, 5], [2, 3], [4, 3]]

for lpnb in range(len(kanony)):

    # a) do A B dám čís. kanónu, jedu úhlopříčky
    a = kanony [lpnb] [1]
    b = kanony [lpnb] [0]

    print(a, b)
    zahrada[a][b] = lpnb

zahrada = np.flip(zahrada, 0)
print(zahrada)

for lpnb in range(len(kanony)):
    kanon = kanony[lpnb]
    
