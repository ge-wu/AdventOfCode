def read_file():
    nums = []
    with open("./09.input") as file:
        for line in file:
            nums.append(int(line.strip()))
    return nums


def part1(nums, preamble_len):
    for i in range(preamble_len, len(nums) - 1, 1):
        ok = True
        for j in range(i - preamble_len, i, 1):
            for k in range(j + 1, i, 1):
                if nums[i] == nums[k] + nums[j]:
                    ok = False
        if ok:
            return nums[i]
    return -1


def part2(nums, target):
    total = 0
    i = 0
    q = []
    while i < len(nums):
        if total < target:
            q.append(nums[i])
            total += nums[i]
            i += 1
        elif total > target:
            while q and total > target:
                total -= q.pop(0)
        else:
            break
    a = float("inf")
    b = float("-inf")
    while q:
        a = min(a, q[0])
        b = max(b, q[0])
        q.pop(0)
    return a + b


def runner():
    nums = read_file()
    part1_ans = part1(nums, 25)

    print("Part 1:", part1_ans)
    print("Part 2:", part2(nums, part1_ans))


if __name__ == '__main__':
    runner()
