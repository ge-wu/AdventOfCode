file = open("01.input")
data = file.readline()

floor = 0
first_enter_basement = len(data) + 1
for i, c in enumerate(data):
    floor = floor + 1 if c == '(' else floor - 1
    if floor == -1 and first_enter_basement == len(data) + 1:
        first_enter_basement = i + 1
print("Part 1:", floor)
print("Part 2:", first_enter_basement)
