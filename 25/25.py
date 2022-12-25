inp = open("25/input.txt").read().splitlines()
total = sum([sum([5**i * ('=-012'.find(c)-2) for i,c in enumerate(line[::-1])]) for line in inp])
b5, final = [total // 5**i % 5 for i in range(100)[::-1]], []

for i in reversed(range(1, len(b5))):
    b5[i-1] += int(b5[i] > 2)
    b5[i] = "=-012"[b5[i]-3]

print(''.join(map(str, b5)).lstrip('0'))

# 7 lines