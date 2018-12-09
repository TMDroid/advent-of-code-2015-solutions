from functools import reduce

with open("input") as f:
    content = f.readlines()

total = 0
ribbonTotal = 0
for dimensions in content:
    d = list(map(lambda x: int(x), dimensions.split("x")))

    #1
    sides = [d[0] * d[1], d[1] * d[2], d[0] * d[2]]
    sides.append(min(sides))
    for side in range(0, len(sides) - 1):
        sides[side] *= 2

    total += sum(sides)

    #2
    biggest = max(d)
    d.remove(biggest)
    ribbon = reduce(lambda x, y: x + x + y + y, d)
    d.append(biggest)
    bowtie = reduce(lambda x, y: x * y, d)

    ribbonTotal += ribbon + bowtie


print("square feet of wrapping paper: {0}".format(total))
print("feet of ribbon : {0}".format(ribbonTotal))
