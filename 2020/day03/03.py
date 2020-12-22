forest = []
part2_pairs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

with open("./03.input") as file:
    for line in file:
        forest.append(line.strip())


def travel_forest(grid, h, v):
    n = len(grid)
    m = len(grid[0])
    x = 0
    y = 0
    ans = 0
    while x < n:
        ans += (grid[x][y] == '#')
        x += v
        y = (y + h) % m
    return ans


print("Part 1:", travel_forest(forest, 3, 1))

ans2 = 1
for x, y in part2_pairs:
    ans2 *= travel_forest(forest, x, y)

print("Part 2:", ans2)
