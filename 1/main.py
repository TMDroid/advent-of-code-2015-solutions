with open("input") as f:
    content = f.readlines()[0]

currentFloor = 0
currentIndex = 0
for c in content:
    currentFloor += (1 if c == '(' else -1)
    currentIndex += 1
    if currentFloor == -1:
        print("Floor is -1: {0}".format(currentIndex))
        break
