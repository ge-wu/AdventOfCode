file = open("./25.input")
A = int(file.readline())
B = int(file.readline())

p = 20201227
g = 7

b = 0
while pow(g, b, p) != B:
    b += 1

print(pow(A, b, p))

