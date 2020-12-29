def collect_data():
    ans = {}
    val = -1
    cur_tile = []
    with open("./20.input") as file:
        for line in file:
            line = line.strip()
            if not len(line):
                ans[val] = cur_tile
                cur_tile = []
            elif "Tile" in line:
                val = int(line.rstrip(':').split()[1])
            else:
                cur_tile.append(line)
    ans[val] = cur_tile
    return ans


def get_border(tile):
    return [
        tile[0], ''.join([t[-1] for t in tile]),
        tile[-1], ''.join(t[0] for t in tile)
    ]


def generate_dihedral(tile):
    # r: rotation
    # f: flip
    # tile: identity
    r = [tile[-1][::-1], tile[0], tile[1][::-1], tile[2]]
    r2 = [tile[2][::-1], tile[-1][::-1], tile[0][::-1], tile[1][::-1]]
    r3 = [tile[1], tile[2][::-1], tile[-1], tile[0][::-1]]
    f1 = [tile[2], tile[1][::-1], tile[0], tile[-1][::-1]]
    f2 = [r[2], r[1][::-1], r[0], r[-1][::-1]]
    f3 = [r2[2], r2[1][::-1], r2[0], r2[-1][::-1]]
    f4 = [r3[2], r3[1][::-1], r3[0], r3[-1][::-1]]

    return [tile, r, r2, r3, f1, f2, f3, f4]


def solve_puzzle(tiles, board, used, size):
    for i in range(size):
        for j in range(size):
            if not board[i][j]:
                for n, borders in tiles.items():
                    if n in used:
                        continue
                    used.append(n)
                    for b in borders:
                        if is_valid(board, i, j, b):
                            board[i][j] = (n, b)
                            if solve_puzzle(tiles, board, used, size):
                                return True
                            else:
                                board[i][j] = None
                    used.remove(n)
                return False
    return True


def is_valid(board, i, j, tile):
    # 0: up, 1: right, 2: down, 3: left
    n = len(board)
    if i == 0 and j == 0:               # top left
        return True
    elif i == 0 and j == n - 1:         # top right
        temp = board[i][j - 1][1]
        return temp[1] == tile[3]
    elif i == n - 1 and j == 0:         # bottom left
        temp = board[i - 1][j][1]
        return temp[2] == tile[0]
    elif i == n - 1 and j == n - 1:     # bottom right
        temp1 = board[i - 1][j][1]
        temp2 = board[i][j - 1][1]
        return temp1[2] == tile[0] and temp2[1] == tile[3]
    elif i == 0:                        # top boarder
        temp = board[i][j - 1][1]
        return temp[1] == tile[3]
    elif i == n - 1:                    # bottom boarder
        temp1 = board[i - 1][j][1]
        temp2 = board[i][j - 1][1]
        return temp1[2] == tile[0] and temp2[1] == tile[3]
    elif j == 0:                        # left boarder
        temp = board[i - 1][j][1]
        return temp[2] == tile[0]
    elif j == n - 1:                    # right boarder
        temp1 = board[i - 1][j][1]
        temp2 = board[i][j - 1][1]
        return temp1[2] == tile[0] and temp2[1] == tile[3]
    else:                               # middle tile
        temp1 = board[i - 1][j][1]         # up
        temp3 = board[i][j - 1][1]         # left
        return temp1[2] == tile[0] and temp3[1] == tile[3]


def runner():
    data = collect_data()
    n = int(len(data) ** 0.5)
    for k, v in data.items():
        four_boarder = get_border(v)
        dihedral_boarders = generate_dihedral(four_boarder)
        data[k] = dihedral_boarders

    used = []
    board = [[None] * n for _ in range(n)]
    foo = solve_puzzle(data, board, used, n)
    a, b, c, d = used[0], used[n - 1], used[n * n - n], used[-1]
    print("Part 1:", a * b * c * d)


if __name__ == '__main__':
    runner()
