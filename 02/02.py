games = [(ord(a)-65, ord(b)-88) for a,b in map(str.split, open('02/input.txt').readlines())]
p1,p2 = [0,3,6],[1,2,3]

print(sum(p2[b] + (p1[1-a:]+p1[:1-a])[b] for a,b in games)) # task 1
print(sum(p1[b] + (p2[b-1:]+p2[:b-1])[a] for a,b in games)) # task 2

# 4 lines