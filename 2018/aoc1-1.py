
y = 0
f = open("input1", "r")

f1 = f.readlines()
for x in f1:
    z = x.split("-+")
    if z[0] == '-':
        y -= int(z[1])
    else:
        y += int(z[1])

print(y)
