directions = open("03.input", 'r').readline()
visited = set()
x, y = 0, 0
for d in directions:
    visited.add((x, y))
    if d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == '^':
        y += 1
    else:
        y -= 1

print("Part 1:", len(visited))

x, y = 0, 0
xr, yr = 0, 0
visited.clear()
for i in range(0, len(directions), 2):
    santa = directions[i]
    robot = directions[i + 1]
    visited.add((x, y))
    visited.add((xr, yr))

    if santa == '>':
        x += 1
    elif santa == '<':
        x -= 1
    elif santa == '^':
        y += 1
    else:
        y -= 1

    if robot == '>':
        xr += 1
    elif robot == '<':
        xr -= 1
    elif robot == '^':
        yr += 1
    else:
        yr -= 1

    if i == len(directions) - 2:
        visited.add((x, y))
        visited.add((xr, yr))

print("Part 2:", len(visited))