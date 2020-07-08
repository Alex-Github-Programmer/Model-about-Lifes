from random import random
m = n = 5
p = 0.5
while True:
    grid = []
    grid.append((n + 4) * [0])
    grid.append((n + 4) * [0])
    for i in range(m):
        grid.append([0, 0])
        for j in range(n):
            grid[-1].append(1 if random() < p else 0)
        grid[-1].extend([0, 0])
    grid.append((n + 4) * [0])
    grid.append((n + 4) * [0])
    flag = True
    for i in range(1, m + 3):
        for j in range(1, n + 3):
            neighbor = grid[i - 1][j - 1] + \
                       grid[i - 1][j] + \
                       grid[i - 1][j + 1] + \
                       grid[i][j - 1] + \
                       grid[i][j + 1] + \
                       grid[i + 1][j - 1] + \
                       grid[i + 1][j] + \
                       grid[i + 1][j + 1]
            if grid[i][j] == 1:
                if neighbor not in [2, 3]:
                    flag = False
                    break
            else:
                if neighbor == 3:
                    flag = False
                    break
        if flag == False:
            break
    if flag == True:
        for i in range(0, m + 4):
            for j in range(0, n + 4):
                print(end = 'o' if grid[i][j] == 1 else '.')
            print()
