inp = open("14/input.txt").read().splitlines()
walls = [[eval(coord) for coord in line.split('->')] for line in inp]
depth, cave = 0, [['.' for _ in range(1000)] for _ in range(300)]

for segment in walls:
    for i in range(1, len(segment)):
        (a,b), (c,d) = segment[i-1], segment[i]
        depth = max(depth, max(b,d))
        for y in range(min(b,d), max(b,d)+1):
                cave[y][a] = '#'
        for x in range(min(a,c), max(a,c)+1):
                cave[b][x] = '#'      

t1, t2, cave[depth+2] = 999999, 0, ['#' for _ in range(1000)]

while cave[0][500] != 'o':
    x, y, t2 = 500, 0, t2 + 1

    while y < depth+2:
        a,b,c = [int(tile != '.') for tile in cave[y+1][x-1:x+2]]
        if sum([a,b,c]) == 3:
            break
        x, y = x + b*([a,b,c].index(0)-1), y + 1

    t1 = min(t2-1, t1) if y > depth else t1 
    cave[y][x] = 'o'

print(t1, t2) # task 1 and 2

# 22 lines