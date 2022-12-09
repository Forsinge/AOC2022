inp = [list(map(int, line)) for line in open('8/input.txt').read().split('\n')]
rot = list(map(list, (zip(*inp[::-1]))))
rows, cols, count_vis, scenery = len(inp), len(inp[0]), 0, []

for i in range(rows):
    for j,h in enumerate(inp[i]):
        dirs = inp[i][:j][::-1], rot[j][rows-i:], inp[i][j+1:], rot[j][:rows-i-1][::-1]
        scenery.append([next(k+1 for k,y in enumerate(d[:-1]+[9]) if y >= h) for d in dirs])
        count_vis += any([max(d+[-1]) < h for d in dirs])

print(count_vis, max(eval(str(tuple(s)).replace(',','*')) for s in scenery)) # task 1 and 2

# 9 lines