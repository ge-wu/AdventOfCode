import time

start_time = time.time()
ans = 0
passports = []
cur_passport = {}
ids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

with open("./04.input") as file:
    for line in file:
        line = line.strip()
        if not line:
            passports.append(cur_passport)
            cur_passport = {}
        else:
            temp = line.split()
            for i in temp:
                k, v = i.split(':')
                cur_passport[k] = v
    passports.append(cur_passport)

ans1 = 0
ans2 = 0
for p in passports:
    if all(i in p for i in ids):
        ans1 += 1
        byr = p["byr"]
        iyr = p["iyr"]
        eyr = p["eyr"]
        pid = p["pid"]
        hgt = p["hgt"]
        hcl = p["hcl"]
        ecl = p["ecl"]
        if 1920 <= int(byr) <= 2002 \
                and 2010 <= int(iyr) <= 2020 \
                and 2020 <= int(eyr) <= 2030 \
                and len(pid) == 9 and all(c in "0123456789" for c in pid) \
                and (("cm" in hgt and 150 <= int(hgt[:-2]) <= 193)
                     or ("in" in hgt and 59 <= int(hgt[:-2]) <= 76)) \
                and len(hcl) == 7 and all(c in "#0123456789abcdef" for c in hcl) \
                and ecl in eye_colors:
            ans2 += 1

print("Part 1:", ans1)  # 254
print("Part 2:", ans2)  # 184
print(f"Execute time: {round((time.time() - start_time), 4)} ms")
