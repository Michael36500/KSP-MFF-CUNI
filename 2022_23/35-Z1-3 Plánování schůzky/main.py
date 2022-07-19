# import
from tqdm import tqdm

# načtu vstup
inputf = "2022_23/35-Z1-3 Plánování schůzky/03.in"
file = open(inputf, "r")

# zjistím počet organizátorů
pocet = int(file.readline())

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

print("read")
for a in tqdm(range(pocet)):
    read_dny()


maximum = 0
print("maximum")
for a in tqdm(organ):
    for b in a:
        if b > maximum:
            maximum = b

dny = []

print("pole")
dny = [0] * (maximum + 1)
# for _ in tqdm(range(maximum + 1)):
#     dny.append(0)


print("change pole")
for a in tqdm(organ):
    # print(a[0], a[1])
    for b in tqdm(range(a[0], a[1] + 1)):
        dny[b] = dny[b] + 1

# print(dny)


wrote = "2022_23/35-Z1-3 Plánování schůzky/out.txt"
escribo = open(wrote, "w")

escribo.write(str(dny.index(max(dny))))
escribo.write(" ")
escribo.write(str(max(dny)))

# # print(max(dny) - 1)
# # print((dny[max(dny) + 1]))