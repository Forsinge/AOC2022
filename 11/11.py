import math

def run(n, expr):
    monkeys, lcm = [], 1

    for ls in [group.splitlines() for group in groups]:
        monkeys.append([eval('[' + ls[1][18:] + ']'), ls[2][19:]] + [int(l[-2:]) for l in ls[3:]] + [0])
        lcm = monkeys[-1][2] * lcm // math.gcd(monkeys[-1][2], lcm)

    for _ in range(n):
        for monkey in monkeys:
            while monkey[0]:
                old, monkey[5] = monkey[0].pop(), monkey[5] + 1
                new = eval('(' + monkey[1] + ')' + expr) % lcm
                monkeys[monkey[4-int(new%monkey[2]==0)]][0].append(new)

    return math.prod(sorted([monkey[5] for monkey in monkeys])[-2:])

groups = open('11/input.txt').read().split('\n\n')
print(run(20, " // 3"), run(10000, "")) # task 1 and 2

# 15 lines