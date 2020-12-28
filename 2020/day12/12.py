import math


def read_files():
    data = []
    with open("./12.input") as file:
        for line in file:
            data.append(line.strip())
    return data


def part1(actions):
    head = x = y = 0
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for act in actions:
        cmd = act[0]
        val = int(act[1:])
        if cmd == 'F':
            x += val * dirs[head][0]
            y += val * dirs[head][1]
        elif cmd == 'L' or cmd == 'R':
            head = (head + val // 90) if cmd == 'L' else (head - val // 90)
            head %= 4
        else:
            if cmd == 'W':
                x -= val
            elif cmd == 'N':
                y += val
            elif cmd == 'E':
                x += val
            else:
                y -= val
    return abs(x) + abs(y)


def part2(actions):
    x = y = 0
    wp_x, wp_y = 10, 1
    for act in actions:
        cmd = act[0]
        val = int(act[1:])
        if cmd == 'F':
            x += val * wp_x
            y += val * wp_y
        elif cmd == 'L' or cmd == 'R':
            s = int(math.sin(val * math.pi / 180))
            c = int(math.cos(val * math.pi / 180))
            temp_x, temp_y = wp_x, wp_y
            rotation = 1 if cmd == 'R' else -1
            wp_x = temp_x * c + rotation * temp_y * s
            wp_y = temp_y * c - rotation * temp_x * s
        else:
            if cmd == 'W':
                wp_x -= val
            elif cmd == 'N':
                wp_y += val
            elif cmd == 'E':
                wp_x += val
            else:
                wp_y -= val
    return abs(x) + abs(y)


def runner():
    data = read_files()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == '__main__':
    runner()
