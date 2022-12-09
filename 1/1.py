sums = sorted(sum(map(int, elf.split())) for elf in open('1/input.txt').read().split('\n\n'))

print(sums[-1], sum(sums[-3:])) # task 1 and 2

# 2 lines