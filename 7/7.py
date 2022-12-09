cmds = map(str.split, open('7/input.txt').readlines() + ['$ cd extra'])
stack, final, size = [], [], 0

for tokens in cmds:
    if tokens[0].isdigit():
        size += int(tokens[0])
    elif tokens[1] == 'cd':
        stack, size = [d+size for d in stack], 0
        stack = stack + [0] if tokens[2] != '..' else stack
        final = final + [stack.pop()] if tokens[2] == '..' else final

print(sum([d for d in (stack + final) if d <= 100000])) # task 1
print(min([d for d in (stack + final) if d >= stack[0]-40000000])) # task 2

# 11 lines