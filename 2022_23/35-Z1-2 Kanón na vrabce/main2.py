# importování numpy (lepší operace s poli)
import numpy as np

# nastavení výšky a šířky pole
x = 6 # výška
y = 6 # šířka

# generuji pole polí o velikosti zahrady +1 (kanóny nejsou v čtverečku, ale na jeho rohu)
zahrada = np.zeros((x + 1, y + 1))

# odečtu od všeho 1
zahrada -= 1

# pole s kanóny
kanony = [[1, 2], [4, 5], [2, 3], [4, 3]]

# loop co dává kanóny do pole / zahrady
for lpnb in range(len(kanony)):

    # do A a B loadnu pozici kanónu
    a = kanony [lpnb, 1]
    b = kanony [lpnb, 0]

    # na dané pozice umístím kanón
    zahrada[a][b] = lpnb


# připravím si pole na výstup
out = []

# loop po jedné úhlopříčdě \ jestli tam není nějaký kanón

for lpnb in range(len(kanony)):
    kanon = kanony[lpnb]    # loadnu si kanón
    start_y = kanon[1] - kanon[0]   # najdu si začáteční Y/výšku.
    act_y = start_y # a zkopíruji si do aktuálnáY pro možnost měnění bez ztráty původní hodnoty

    # nastavení pár proměných
    closest_before = None   # zde se zapíše nejbližší kanón před aktuálním kanónem
    closest_after = None    # zde se zapíše nejbližší kanón za aktuálním kanónem
    after_thisone = False   # bool pro to, jestli jsem před
    tempup = []

