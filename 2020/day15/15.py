import time


def nth_most_recent_spoken(nums, n):
    nums.append(0)
    seen = [0] * 100000000
    for i in range(len(nums) - 1):
        seen[nums[i]] = i + 1

    for i in range(len(nums), n):
        most_recent_num = nums[i - 1]
        temp = i - seen[most_recent_num] if seen[most_recent_num] != 0 else 0
        nums.append(temp)
        seen[most_recent_num] = i
    return nums[n-1]


start_time = time.time()
lst = [7, 12, 1, 0, 16, 2]
print("Part 1:", nth_most_recent_spoken(lst, 2020))
print("Part 2:", nth_most_recent_spoken(lst, 30000000))
print(f"Execute time: {round((time.time() - start_time), 4)} s")

