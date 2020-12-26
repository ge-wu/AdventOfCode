def read_file():
    with open("./13.input") as file:
        num = int(file.readline().strip())
        notes = file.readline().strip().split(',')
    return num, notes


def part1(num, notes):
    ans = float("inf")
    bus_id = 0
    for note in notes:
        if note != 'x':
            note = int(note)
            cur = num - num % note + note
            if cur < ans:
                ans = cur
                bus_id = note
    return (ans - num) * bus_id


def part2(notes):
    # Part II
    # Let t be the solution of part II. Then we can derive that t % 41 == 0,
    # (t + 35) % 37 == 0, because there are 34 x's between 41 and 37 in the
    # input and so on ... Finally we will have:
    #
    # t        = 0 mod 41   =>  t = 0     mod 41
    # t + 35   = 0 mod 37   =>  t = 2     mod 37
    # t + 41   = 0 mod 557  =>  t = 516   mod 557
    # t + 43   = 0 mod 29   =>  t = 15    mod 29
    # t + 54   = 0 mod 13   =>  t = 11    mod 13
    # t + 58   = 0 mod 17   =>  t = 10    mod 17
    # t + 64   = 0 mod 23   =>  t = 5     mod 23
    # t + 72   = 0 mod 419  =>  t = 347   mod 419
    # t + 91   = 0 mod 19   =>  t = 4     mod 19
    # ('=' actually mean equivalent)
    #
    # Therefore, it is just a Chinese remainder theorem problem. Since there are
    # primes in module n, so that there is a solution of this problem.
    pairs = [[-i % int(note), int(note)]
             for i, note in enumerate(notes) if note != 'x']
    mod = 1
    ans = 0
    for a, m in pairs:
        mod *= m

    for a, m in pairs:
        b = mod // m
        ans += a * b * pow(b, m - 2, m)
        ans %= mod
    return ans


def runner():
    nums, notes = read_file()
    ans1 = part1(nums, notes)
    ans2 = part2(notes)
    print("Part 1:", ans1)
    print("Part 2:", ans2)


if __name__ == '__main__':
    runner()