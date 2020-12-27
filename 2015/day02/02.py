dimensions = []

with open("./02.input") as file:
    for line in file:
        line = map(int, line.strip().split('x'))
        dimensions.append(list(line))


def calc_surface_area(dimension):
    dimension = sorted(dimension)
    a, b, c = dimension
    return 2 * (a * b + b * c + c * a) + a * b


def calc_ribbon_len(dimension):
    dimension = sorted(dimension)
    a, b, c = dimension
    return a * 2 + b * 2 + a * b * c


ans1 = sum(calc_surface_area(d) for d in dimensions)
ans2 = sum(calc_ribbon_len(d) for d in dimensions)
print("Part 1:", ans1)
print("Part 2:", ans2)
