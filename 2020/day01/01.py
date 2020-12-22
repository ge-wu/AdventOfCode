import time

start_time = time.time()
data = []
with open("./01.input") as file:
    for line in file:
        data.append(int(line.strip()))

n = len(data)
for i in range(n):
    for j in range(i+1, n):
        if data[i] + data[j] == 2020:
            print("Part 1:", data[i] * data[j])
        for k in range(j+1, n):
            if data[i] + data[j] + data[k] == 2020:
                print("Part 2:", data[i] * data[j] * data[k])

print(f"Execute time: {round((time.time() - start_time), 4)} s")
