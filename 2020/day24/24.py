identifiers = []
with open("./24.input") as file:
    for line in file:
        identifiers.append(line.strip())

directions = {"w": [0, -1, 1], "e": [0, 1, -1], "nw": [1, -1, 0],
              "ne": [1, 0, -1], "se": [-1, 1, 0], "sw": [-1, 0, 1]}


def flip_tiles(ids: list) -> set:
    black_pos = set()
    for k in range(len(ids)):
        i = 0
        x, y, z = 0, 0, 0
        while i < len(ids[k]):
            cur = ids[k][i]
            if cur == 'n' or cur == 's':
                cur += ids[k][i + 1]
                i += 1
            a, b, c = directions[cur]
            x, y, z = x + a, y + b, z + c
            i += 1
        if (x, y, z) in black_pos:
            black_pos.remove((x, y, z))
        else:
            black_pos.add((x, y, z))
    return black_pos


def daily_update(tiles_pos: set) -> set:
    new = set()
    for (x, y, z) in tiles_pos:
        new.add((x, y, z))
        for (i, j, k) in directions.values():
            new.add((x + i, y + j, z + k))

    ans = set()
    for (x, y, z) in new:
        black_cnt = sum(1 for i, j, k in directions.values()
                        if (x + i, y + j, z + k) in tiles_pos)

        if (x, y, z) in tiles_pos and (black_cnt == 1 or black_cnt == 2):
            ans.add((x, y, z))
        if (x, y, z) not in tiles_pos and black_cnt == 2:
            ans.add((x, y, z))
    return ans


black_tiles = flip_tiles(identifiers)
print("Part 1:", len(black_tiles))

for _ in range(100):
    black_tiles = daily_update(black_tiles)

print("Part 2:", len(black_tiles))

