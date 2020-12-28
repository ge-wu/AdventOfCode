def read_file():
    data = []
    with open("./06.input") as file:
        for line in file:
            data.append(line.strip())
    return data


def part1(data):
    cur = set()
    ans = 0
    for d in data:
        if d != '':
            cur |= set(list(d))
        else:
            ans += len(cur)
            cur.clear()
    return ans + len(cur)


def part2(data):
    ans = 0
    group_size = 0
    cnt = [0] * 26
    for d in data:
        if d != '':
            group_size += 1
            for c in d:
                cnt[ord(c) - 97] += 1
        else:
            ans += cnt.count(group_size)
            cnt = [0] * 26
            group_size = 0
    return ans


def runner():
    data = read_file()
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == '__main__':
    runner()
