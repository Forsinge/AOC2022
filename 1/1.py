with open('1/input.txt') as f:
    sums = [sum([int(item) for item in elf.splitlines()]) for elf in f.read().split('\n\n')]
    print(sums.sort(), sums[-1], sum(sums[-3:])) # task 1 and 2