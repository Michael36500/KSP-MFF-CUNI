# import
from tqdm import tqdm

# načtu vstup
inputf = "2022_23/35-Z1-3 Plánování schůzky/vstup"
file = open(inputf, "r")

# zjistím počet organizátorů
pocet = int(file.readline())

print(pocet)

# import pole s volnými dny
organ = []
def read_dny():
    global file
    global organ

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

    temp = []
    temp.append(x)
    temp.append(y)
    # temp.append(lp)

    organ.append(temp)

for a in range(pocet):
    read_dny()

print(max(organ))  

dny = []

for _ in range(max(organ)):
    dny.append(0)

print(dny)