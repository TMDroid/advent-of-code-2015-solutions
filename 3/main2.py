with open("input") as f:
    content = f.readlines()[0]

size = 200
xRobo = x = int(size / 2)
yRobo = y = int(size / 2)

grid = [[0 for a in range(size)] for b in range(size)]

grid[y][x] += 1

multivisit = 0
turn = 1  # if 1 then move santa else if 0 move robosanta
for character in content:
    if character == '<':
        action = (-1, 0)
    elif character == '>':
        action = (1, 0)
    elif character == '^':
        action = (0, -1)
    else:
        action = (0, 1)

    if turn == 1:
        x += action[0]
        y += action[1]

        grid[y][x] += 1
        turn = 0
    else:
        xRobo += action[0]
        yRobo += action[1]

        grid[yRobo][xRobo] += 1
        turn = 1

for i in range(size):
    row = grid[i]

    for j in range(size):
        cell = grid[i][j]

        if cell > 0:
            multivisit += 1

print(multivisit)
