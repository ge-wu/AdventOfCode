neighbors_3d = [
    (x, y, z)
    for x in range(-1, 2)
    for y in range(-1, 2)
    for z in range(-1, 2)
    if x != 0 or y != 0 or z != 0
]

neighbors_4d = [
    (w, x, y, z)
    for w in range(-1, 2)
    for x in range(-1, 2)
    for y in range(-1, 2)
    for z in range(-1, 2)
    if w != 0 or x != 0 or y != 0 or z != 0
]

grid = []
with open("./17.input") as file:
    for line in file:
        grid.append(line.strip())


def cycle_simulation_3d(_cubes: dict) -> dict:
    ans = {}
    for k, v in _cubes.items():
        x, y, z = k
        cur_neighbors = [(x + _x, y + _y, z + _z)
                         for _x, _y, _z in neighbors_3d]
        cnt = sum(1 for t in cur_neighbors if _cubes.get(t) == '#')

        if v == '#':
            ans[k] = '#' if cnt == 3 or cnt == 2 else '.'

            for a, b, c in cur_neighbors:
                if (a, b, c) not in _cubes:
                    cur_neighbors2 = [(a + _a, b + _b, c + _c)
                                      for _a, _b, _c in neighbors_3d]
                    cnt2 = sum(1 for t in cur_neighbors2
                               if _cubes.get(t) == '#')
                    if cnt2 == 3:
                        ans[(a, b, c)] = '#'
        else:
            ans[k] = '#' if cnt == 3 else '.'
    return ans


n, m = len(grid), len(grid[0])
cubes = {(i, j, 0): grid[i][j] for i in range(n) for j in range(m)}

for _ in range(6):
    cubes = cycle_simulation_3d(cubes)

print("Part 1:", list(cubes.values()).count('#'))

cubes = {(i, j, 0, 0): grid[i][j] for i in range(n) for j in range(m)}


def cycle_simulation_4d(_cubes: dict) -> dict:
    ans = {}
    for k, v in _cubes.items():
        w, x, y, z = k
        cur_neighbors = [(w + _w, x + _x, y + _y, z + _z)
                         for _w, _x, _y, _z in neighbors_4d]
        cnt = sum(1 for t in cur_neighbors if _cubes.get(t) == '#')

        if v == '#':
            ans[k] = '#' if cnt == 3 or cnt == 2 else '.'

            for a, b, c, d in cur_neighbors:
                if (a, b, c, d) not in _cubes:
                    cur_neighbors2 = [(a + _a, b + _b, c + _c, d + _d)
                                      for _a, _b, _c, _d in neighbors_4d]
                    cnt2 = sum(1 for t in cur_neighbors2
                               if _cubes.get(t) == '#')
                    if cnt2 == 3:
                        ans[(a, b, c, d)] = '#'
        else:
            ans[k] = '#' if cnt == 3 else '.'
    return ans


for _ in range(6):
    cubes = cycle_simulation_4d(cubes)

print("Part 2:", list(cubes.values()).count('#'))
