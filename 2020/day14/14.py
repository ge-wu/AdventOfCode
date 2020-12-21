import itertools
import time


start_time = time.time()
mask0 = ""
mask1 = ""
mem1 = {}

with open("./14.input") as file:
    for line in file:
        line = line.strip()
        if "mask" in line:
            mask0 = int(line.split()[2].replace('X', '0'), 2)
            mask1 = int(line.split()[2].replace('X', '1'), 2)
        else:
            temp = line.split()
            address = int(''.join(filter(str.isdigit, temp[0])))
            val = int(temp[2])
            mem1[address] = mask0 | mask1 & val

print("Part 1:", sum(mem1.values()))    # 13476250121721

# Ugly code. Please don't try to understand it.
mask = ""
mem = {}
with open("./14.input") as file:
    for line in file:
        line = line.strip()
        if "mask" in line:
            mask = line.split()[2]
        else:
            temp = line.split()
            address = ''.join(filter(str.isdigit, temp[0]))  # get address
            bin_address = bin(int(address))[2:].zfill(36)    # convert to bin
            val = int(temp[2])

            masked_address = ""
            # Mask the address
            for i in range(36):
                if mask[i] == 'X':
                    masked_address += 'X'
                else:
                    masked_address += str(int(mask[i]) | int(bin_address[i]))
            # Get all combination of 0 and 1 with number of X's.
            combs = itertools.product([0, 1], repeat=masked_address.count('X'))

            for comb in combs:
                idx, dec = 0, 0
                for i in range(35, -1, -1):
                    if masked_address[i] == 'X':
                        dec += (comb[idx] * 2 ** (35 - i))
                        idx += 1
                    else:
                        dec += (int(masked_address[i]) * 2 ** (35 - i))
                mem[dec] = val

print("Part 2:", sum(mem.values()))     # 4463708436768
print(f"Execute time: {round((time.time() - start_time), 4)} ms")
