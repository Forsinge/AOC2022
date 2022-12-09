lines = map(str.split, open('9/input.txt').read().split('\n'))
move = lambda z: round(z.real / 1.99) + round(z.imag / 1.99) * 1j
directions, path = {"L": -1, "R": 1, "U": 1j, "D": -1j}, [0]
[[path.append(path[-1] + directions[d]) for _ in range(int(n))] for d,n in lines]

def run(tails, path, trail):
    [[trail.append(t + move(h-t) * int(abs(h-t) >= 2))] for h,t in zip(path, trail)]
    return run(tails-1, trail, [0]) if tails-1 > 0 else len(set(trail))

print(run(1, path, [0]), run(9, path, [0])) # task 1 and 2

# 8 lines