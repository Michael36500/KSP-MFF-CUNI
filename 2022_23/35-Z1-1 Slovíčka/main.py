inputf = "2022_23/35-Z1-1 Slovíčka/vstup"
file = open(inputf, "r")

print(int(file.read(1)))





file.close()

inp = ["platypus", "pig", "porcupine", "rhinoceros", "rabbit", "possum", "panda"]

first = "pig"
last = "rhinoceros"

sort = sorted(inp)
print(sort)

whfirst = sort.index(first)
whlast = sort.index(last)

if whlast - whfirst >= 0:
    print(whlast - whfirst - 1)
else:
    print(whfirst - whlast - 1)