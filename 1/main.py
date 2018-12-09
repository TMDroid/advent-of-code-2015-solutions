with open("input") as f:
    content = f.readlines()[0]

currentFloor = 0
for c in content:
    currentFloor += (1 if c == '(' else -1)

print(currentFloor)
