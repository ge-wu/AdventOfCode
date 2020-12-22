import time

start_time = time.time()
ansI = 0
ansII = 0
with open("./02.input") as file:
    for line in file:
        line = line.strip()
        cnt, char, password = line.split()
        a, b = map(int, cnt.split('-'))
        ansI += a <= password.count(char[:-1]) <= b
        ansII += (password[a-1] == char[:-1]) ^ (password[b-1] == char[:-1])

print("Part 1:", ansI)
print("Part 2:", ansII)
print(f"Executive time: {round(time.time() - start_time, 4)} s")
