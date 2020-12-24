data = []
with open("./18.input") as file:
    for line in file:
        data.append(line.strip())


def evl_exp(exp: str) -> int:
    ans = 0
    num = 0
    cur_ope = '+'
    for i in range(len(exp)):
        c = exp[i]
        if c.isdigit():
            num = num * 10 + int(c)
        if not c.isdigit() and c != ' ' or i == len(exp) - 1:
            ans = ans + num if cur_ope == '+' else ans * num
            num = 0
            cur_ope = c
    return ans


def advance_evl_exp(exp: str) -> int:
    stack = []
    num = 0
    ans = 1
    cur_ope = '+'
    for i in range(len(exp)):
        c = exp[i]
        if c.isdigit():
            num = num * 10 + int(c)
        if not c.isdigit() and c != ' ' or i == len(exp) - 1:
            if cur_ope == '+' and stack:
                temp = stack.pop()
                stack.append(temp + num)
            else:
                stack.append(num)
            cur_ope = c
            num = 0
    while stack:
        ans *= stack.pop()
    return ans


def calculator(exp: str, advance_evl=False) -> int:
    stack = []
    cur_str = ""
    for i in range(len(exp)):
        cur = exp[i]
        if cur == '(':
            stack.append(cur_str)
            cur_str = ""
        elif cur == ')':
            if advance_evl:
                cur_str = stack.pop() + str(advance_evl_exp(cur_str))
            else:
                cur_str = stack.pop() + str(evl_exp(cur_str))
        else:
            cur_str += cur
    return advance_evl_exp(cur_str) if advance_evl else evl_exp(cur_str)


print("Part 1:", sum(calculator(i) for i in data))
print("Part 2:", sum(calculator(i, True) for i in data))
