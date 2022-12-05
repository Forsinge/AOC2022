with open('5/input.txt') as f:
    crates, instrs = [section.split('\n') for section in f.read().split('\n\n')]
    stacks = [[c for c in line if c.isalpha()] for line in list(zip(*crates[::-1])) if line[0].isnumeric()]
    copy1, copy2 = [stack[:] for stack in stacks], [stack[:] for stack in stacks]
    for instr in instrs:
        n, fr, to = map(int, instr.split()[1::2])
        copy1[to-1] += [copy1[fr-1].pop() for _ in range(n)]
        copy2[to-1] += reversed([copy2[fr-1].pop() for _ in range(n)])
    print(''.join([stack[-1] for stack in copy1]), ''.join([stack[-1] for stack in copy2])) # task 1 and 2