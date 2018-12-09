with open("input") as f:
    content = f.readlines()

size = 1000
x = int(size / 2)
y = int(size / 2)

grid = [[0 for a in range(size)] for b in range(size)]
grid[y][x] += 1

multivisit = 0
for line in content:
    for character in line:
        if character == '<':
            x -= 1
        elif character == '>':
            x += 1
        elif character == '^':
            y -= 1
        else:
            y += 1

        grid[y][x] += 1

    for i in range(size):
        row = grid[i]

        for j in range(size):
            cell = grid[i][j]

            if cell > 0:
                multivisit += 1

print(multivisit + 1)
