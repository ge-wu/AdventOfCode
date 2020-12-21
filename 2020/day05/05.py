import time

start_time = time.time()
seat_ids = []


def calc_seat_id(seat):
    up, down, right, left = 0, 127, 0, 8
    for c in seat:
        if c == 'F':
            down = (up + down) // 2
        elif c == 'B':
            up = (up + down + 1) // 2
        elif c == 'R':
            right = (right + left + 1) // 2
        else:
            left = (right + left) // 2
    return down * 8 + right


with open("./05.input") as file:
    for line in file:
        seat_ids.append(calc_seat_id(line))

print("Part 1:", max(seat_ids))

seat_ids = sorted(seat_ids)
for i in range(1, len(seat_ids)):
    if seat_ids[i-1] + 2 == seat_ids[i]:
        print("Part 2:", seat_ids[i] - 1)
        break

print(f"Execute time: {round(time.time() - start_time, 4)} s")
