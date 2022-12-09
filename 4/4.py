pairs = [[p.split('-') for p in s.split(',')] for s in open('4/input.txt').readlines()]
ranges = [[set(range(int(l), int(h)+1)) for l,h in pair] for pair in pairs]

print(sum([l>=r or r>=l for l,r in ranges]), sum([len(l&r) != 0 for l,r in ranges])) # task 1 and 2

# 3 lines