import time

start_time = time.time()
graph = {}
with open("./07.input") as file:
    for line in file:
        line = line.strip().split(" contain ")
        color = ' '.join(line[0].split()[:2])
        graph[color] = line[1]


# Glad there is no loop 
def dfs1(cur_color):
    if "shiny gold" in graph[cur_color]:
        return True
    for it in graph[cur_color].split(', '):
        if "no other bags" in it:
            continue
        bag_color = ' '.join(it.split()[1:3])
        if dfs1(bag_color):
            return True
    return False


def dfs2(cur_color):
    if "no other bags" in graph[cur_color]:
        return 0
    temp = 0
    for it in graph[cur_color].split(', '):
        bag_cnt = int(it[0])
        bag_color = ' '.join(it.split()[1:3])
        temp += bag_cnt + (bag_cnt * dfs2(bag_color))
    return temp


ans = 0
for key, val in graph.items():
    if dfs1(key):
        ans += 1

print("Part 1:", ans)                   # 300
print("Part 2:", dfs2("shiny gold"))    # 8030

print(f"Execute time: {round(time.time() - start_time, 4)} s")

