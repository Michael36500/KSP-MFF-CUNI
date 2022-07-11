inputf = "2022_23/35-Z1-1 Slovíčka/vstup"
file = open(inputf, "r")
inp = []

rng = int(file.read(1))

file.readline()

for line in range(rng):
    temp = file.readline()
    temp = temp.replace("\n", "" )
    inp.append(temp)





file.close()

print(inp)

first = "pig"
last = "rhinoceros"

sort = sorted(inp)
# print(sort)

whfirst = sort.index(first)
whlast = sort.index(last)

if whlast - whfirst >= 0:
    print(whlast - whfirst - 1)
else:
    print(whfirst - whlast - 1)