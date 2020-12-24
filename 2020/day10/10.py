adapters = []

with open("./10.input") as file:
    for line in file:
        adapters.append(int(line.strip()))

adapters = sorted(adapters)
adapters = [0] + adapters + [max(adapters) + 3]
cnt = [0, 0, 0, 0]
for i in range(1, len(adapters)):
    cnt[adapters[i] - adapters[i - 1]] += 1

print("Part 1:", cnt[1] * cnt[3])

dp = [1] * len(adapters)
for i in range(2, len(adapters)):
    dp[i] = dp[i - 1]
    if i > 1 and adapters[i] - adapters[i - 2] <= 3:
        dp[i] += dp[i - 2]
    if i > 2 and adapters[i] - adapters[i - 3] <= 3:
        dp[i] += dp[i - 3]

print("Part 2:", dp[-1])
