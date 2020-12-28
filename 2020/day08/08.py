def read_file():
    data = []
    with open("./08.input") as file:
        for line in file:
            ins, val = line.strip().split()
            data.append([ins, int(val)])
    return data


def sum_accumulate(track):
    return sum(t[1] for t in track if t[0] == "acc")


def walk(data):
    seen = [False] * len(data)
    track = []
    i = 0
    while i < len(data) and not seen[i]:
        seen[i] = True
        track.append(data[i])
        ins, val = data[i]
        if ins == "jmp":
            i += val
        else:
            i += 1
    return track


def part2(track):
    last = track[-1]
    temp = None
    for i in range(len(track)):
        cmd, val = track[i]
        if cmd != "acc":
            update = "nop" if cmd == "jmp" else "jmp"
            track[i][0] = update
            temp = walk(track)
            track[i][0] = cmd
        if temp and temp[-1] == last:
            return temp
    return None


def runner():
    data = read_file()
    track1 = walk(data)
    track2 = part2(data)

    print("Part 1:", sum_accumulate(track1))
    print("Part 2:", sum_accumulate(track2))


if __name__ == '__main__':
    runner()
