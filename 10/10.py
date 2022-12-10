cmds, xs = open('10/input.txt').read().replace('addx', 'noop\naddx').split('\n'), [1]

for i,cmd in enumerate(cmds):
    v = 0 if cmd == 'noop' else int(cmd.split()[1])
    xs.append(xs[-1] + v)

print(sum([x*((i+1)*40-20) for i,x in enumerate(xs[20::40])])) # task 1
print(''.join([' █'[abs(x % 40 - i % 40) <= 1] + '\n' * (i % 40 == 39) for i,x in enumerate(xs)])) # task 2

# 6 lines