import collections


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
    return [tile[0], ''.join([t[-1] for t in tile]),
            tile[-1], ''.join(t[0] for t in tile)]


def generate_dihedral(tile, n):
    ans = []
    tile_copy = [list(x) for x in tile]
    for _ in range(n):
        tile_copy = [''.join(x) for x in zip(*tile_copy[::-1])]
        ans.extend([tile_copy, tile_copy[::-1]])
    return ans


def solve_puzzle(tiles, board, used, size):
    for i in range(size):
        for j in range(size):
            if not board[i][j]:
                for n, borders in tiles.items():
                    if n in used:
                        continue
                    used.append(n)
                    for ii, b in enumerate(borders["edges"]):
                        if is_valid(board, i, j, b):
                            # val, num, and index of dihedral
                            board[i][j] = (n, b, ii)
                            if solve_puzzle(tiles, board, used, size):
                                return True
                            else:
                                board[i][j] = None
                    used.remove(n)
                return False
    return True


def is_valid(grid, i, j, border):
    # 0: up, 1: right, 2: down, 3: left
    # Since we are iterate the grid from left to right and from top to bottom.
    # Therefore, we can derive that 1, the top right corner has no constraint.
    # 2, the pieces at the top edge only need to check the piece on its right.
    # 3, the pieces at the left edge only need to check the piece on its top.
    # 4. all other pieces: middle, right edge need to check its top and left.
    if i == 0 and j == 0:
        return True
    elif i == 0:
        left = grid[i][j - 1][1]
        return left[1] == border[3]
    elif j == 0:
        up = grid[i - 1][j][1]
        return up[2] == border[0]
    else:
        left = grid[i - 1][j][1]
        up = grid[i][j - 1][1]
        return left[2] == border[0] and up[1] == border[3]


def is_monster(grid, i, j):
    monster_coords = [
        [1, 1], [1, 4], [0, 5], [0, 6], [1, 7],
        [1, 10], [0, 11], [0, 12], [1, 13], [1, 16],
        [0, 17], [0, 18], [-1, 18], [0, 19]
    ]
    n = len(grid)
    for x, y in monster_coords:
        new_x, new_y = i + x, j + y
        if not(0 <= new_x < n and 0 <= new_y < n) or grid[new_x][new_y] != '#':
            return False
    return True


def runner():
    data = collect_data()
    n = int(len(data) ** 0.5)
    tiles = collections.defaultdict(dict)
    for num, tile in data.items():
        dihedral = generate_dihedral(tile, 4)
        tiles[num]["dihedral"] = dihedral
        tiles[num]["edges"] = [get_border(x) for x in dihedral]

    # part 1
    used = []
    board = [[None] * n for _ in range(n)]
    if solve_puzzle(tiles, board, used, n):
        a, b, c, d = used[0], used[n - 1], used[n * (n - 1)], used[-1]
        print("Part 1:", a * b * c * d)

    # part 2
    solved_puzzle = []
    for i, row in enumerate(board):
        temp = [tiles[val]["dihedral"][idx] for (val, _, idx) in row]
        without_edges = []
        for t in temp:
            without_edges.append([x[1:-1] for x in t[1:-1]])
        solved_puzzle.extend(''.join(t) for t in zip(*without_edges))

    # This part I am not very sure. All orientation will generate 2567, except
    # one that will give 2012, and that is the answer.
    ans = []
    for t in generate_dihedral(solved_puzzle, 4):
        temp = 0
        for i in range(len(t)):
            for j in range(len(t)):
                if t[i][j] == '#':
                    temp += 1
                    if is_monster(t, i, j):
                        temp -= 15
        ans.append(temp)
    print("Part 2:", (7 * sum(set(ans)) - sum(ans)) // 6)


if __name__ == '__main__':
    runner()
