lines = open('3/input.txt').read().split('\n'), 
priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
halves = [map(set, (s[len(s)//2:], s[:len(s)//2])) for s in lines]
triples = [map(set, lines[i:i+3]) for i in range(0, len(lines), 3)]

print(sum(priority.find(min(a & b)) for a,b in halves))        # task 1
print(sum(priority.find(min(a & b & c)) for a,b,c in triples)) # task 2

# 6 lines