# importy
from tqdm import tqdm

# load file
inputf = "2022_23/35-Z1-1 Slovíčka/05.in"
file = open(inputf, "r")

# load slovíčka
inp = []

# přečtu 1. řádek
line = file.readline()
# loop pro najdení počtu slovíček v testu
pomezere = False
rng = ""
for a in line:
    if a == " " and pomezere == False:
        pomezere = not pomezere
        continue
    elif pomezere == False:
        rng = str(rng) + str(a)

# loop přes slovíčka, appenduju do inp
for line in range(int(rng)):
    temp = file.readline()
    temp = temp.replace("\n", "" )
    inp.append(temp)

# uspořádám podle abecedy
sort = sorted(inp)

# loadnu novou filu z stejného txt
tfile = open(inputf, "r")
fline = tfile.readline()

# zjistím počet slovíček v testu
pomezere = False
out = ""

# loop pro najdení počtu slovíček v testu
for a in fline:
    if a == " " and pomezere == False:
        pomezere = True
        continue
    elif pomezere == True:
        out = str(out) + str(a)

# load write file
escribo = open("2022_23/35-Z1-1 Slovíčka/out.txt", "w")

# output list
finalout = []

# main loop
for _ in tqdm(range(int(out))):
    # inicializace slovíček, o kterých věděl, kde jsou
    first = ""
    last = ""

    # loadnu ten řádek s slovíčky, co něvěděl
    line = file.readline()
    line = line.replace("\n", "")

    # appenduju to first a last postupně písmenka, a používám mezeru jako dělič
    pomezere = False
    for a in line:
        if a == " " and pomezere == False:
            pomezere = True
            continue
        elif pomezere == False:
            first = str(first) + str(a)
        elif pomezere == True:
            last = str(last) + str(a)
    
    # print(first, last)

    whfirst = sort.index(first)
    whlast = sort.index(last)

    if whlast - whfirst >= 0:
        finalout.append(whlast - whfirst - 1)
    else:
        finalout.append(whfirst - whlast - 1)

for e in finalout:
    escribo.write(str(e) + "\n")


file.close()
escribo.close()