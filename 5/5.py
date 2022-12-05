with open('5/input.txt') as f:
    crates, instrs = [section.split('\n') for section in f.read().split('\n\n')]
    stacks = [[c for c in line if c.isalpha()] for line in list(zip(*crates[::-1])) if line[0].isnumeric()]
    s1, s2 = [stack[:] for stack in stacks], [stack[:] for stack in stacks]
    for instr in instrs:
        n, fr, to = map(int, instr.split()[1::2])
        m1, m2 = [s1[fr-1].pop() for _ in range(n)], reversed([s2[fr-1].pop() for _ in range(n)])
        s1[to-1] += m1
        s2[to-1] += m2
    print(''.join([stack[-1] for stack in s1]), ''.join([stack[-1] for stack in s2])) # task 1 and 2