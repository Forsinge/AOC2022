crates, instrs = [section.split('\n') for section in open('5/input.txt').read().split('\n\n')]
stacks1 = [list(''.join(line[1:]).strip()) for line in list(zip(*crates[::-1]))[1::4]]
stacks2 = [stack[:] for stack in stacks1]

for instr in instrs:
    n, fr, to = map(int, instr.split()[1::2])
    stacks1[to-1] += [stacks1[fr-1].pop() for _ in range(n)]
    stacks2[to-1] += [stacks2[fr-1].pop() for _ in range(n)][::-1]

print(*[stack[-1] for stack in stacks1], ' ', *[stack[-1] for stack in stacks2]) # task 1 and 2

# 8 lines