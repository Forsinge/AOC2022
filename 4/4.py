with open('4/input.txt') as f:
    pairs = [sorted(list(map(int, pair.split('-'))) for pair in line.split(',')) for line in f.readlines()]
    print(sum([int(b >= d or a == c) for (a,b),(c,d) in pairs])) # task 1
    print(sum([int(b >= c) for (_,b),(c,_) in pairs])) # task 2