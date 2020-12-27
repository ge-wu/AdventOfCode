import hashlib


def read_file():
    file = open("./04.input", 'r')
    return file.readline().strip()


def helper(init, n):
    cur = ""
    i = 0
    while cur[:n] != ('0' * n):
        cur = hashlib.md5((init + str(i)).encode()).hexdigest()
        i += 1
    return i - 1


def runner():
    data = read_file()
    print("Part 1:", helper(data, 5))
    print("Part 2:", helper(data, 6))


if __name__ == '__main__':
    runner()
