with open('2/input.txt') as f:
    p1, p2, matchups = [0,3,6], [1,2,3], [(ord(a)-65, ord(b)-88) for a,b in map(str.split, f.readlines())]
    print(sum(b+1 + (p1[1-a:]+p1[:1-a])[b] for a,b in matchups))
    print(sum(b*3 + (p2[b-1:]+p2[:b-1])[a] for a,b in matchups))