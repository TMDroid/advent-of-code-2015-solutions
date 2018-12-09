with open("input") as f:
    content = f.readlines()

total = 0
for dimensions in content:
    dimensions = dimensions.split("x")
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])

    sides = [l * w, w * h, l * h]
    sides.append(min(sides))
    for side in range(0, len(sides) - 1):
        sides[side] *= 2

    total += sum(sides)

print(total)
