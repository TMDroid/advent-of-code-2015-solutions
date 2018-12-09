import re

with open("input") as f:
    content = f.readlines()

size = 1000
grid = [[0 for a in range(size)] for b in range(size)]

for instruction in content:
    numbers = list(map(lambda x: int(x), re.findall(r'\d+', instruction)))

    if "toggle" in instruction:
        action = "toggle"
    elif "off" in instruction:
        action = "off"
    else:
        action = "on"

    for i in range(numbers[0], numbers[2] + 1):
        for j in range(numbers[1], numbers[3] + 1):
            result = 1 if action == "on" else (-1 if action == "off" else 2)

            if result == -1 and grid[i][j] == 0:
                continue

            grid[i][j] += result

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
            count += grid[i][j]

print(count)
