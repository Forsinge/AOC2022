lines = [[c for c in line if ' -1234567890'.count(c)] for line in open("15/input.txt").readlines()]
scanners = [[int(s) for s in ''.join(line).split()] for line in lines]
edges, diamonds = [], sorted([((sx,sy), abs(sx-bx) + abs(sy-by)) for sx,sy,bx,by in scanners])
i, ranges = 0, sorted([(x-d*(d>0), x+d*(d>0)) for (x,y),r in diamonds if (d := (r-abs(2000000-y)))])

while i < len(ranges)-1:
    i, (a,b), (c,d) = i+1, ranges[i], ranges[i+1]
    i, pop, ranges[i] = i-1, ranges.pop(i), (a, max(b,d)) if b+1 >= c else (i, 0, ranges[i])

for i in range(len(diamonds)):
    for j in range(i+1,len(diamonds)):
        ((x1, y1), r1), ((x2, y2), r2) = diamonds[i], diamonds[j]
        if r1+r2+2 == abs(x2-x1)+abs(y2-y1):
            k = int(y2<y1)-int(y2>y1)
            edges.append(((x2-r2-1, y2), (x2, y2+(r2+1)*k)))

for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        ((ax,ay),(bx,by)), ((cx,cy),(dx,dy)) = edges[i], edges[j]
        div = (ax-bx)*(cy-dy) - (ay-by)*(cx-dx)
        if div:
            x = ((ax*by-ay*bx)*(cx-dx) - (cx*dy-cy*dx)*(ax-bx)) // div
            y = ((ax*by-ay*bx)*(cy-dy) - (cx*dy-cy*dx)*(ay-by)) // div
            if not any([r >= abs(x-sx) + abs(y-sy) for (sx,sy),r in diamonds]):
                if 0 <= x <= 4000000 and 0 <= y <= 4000000:
                    exit(str(sum([hi-lo for lo,hi in ranges])) + ' ' + str(x*4000000+y)) # task 1 and 2

# 23 lines