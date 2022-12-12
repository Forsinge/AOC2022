def bfs(grid, start, end, levels):
    visited, queue, rows, cols = set(), [(0, start)], len(grid), len(grid[0])
    
    while queue:
        dist, (y,x) = queue.pop(0)
        
        if (y,x) == end:
            return dist
        
        for dy,dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            y2, x2 = y+dy, x+dx
            if 0 <= y2 < rows and 0 <= x2 < cols and (y2,x2) not in visited:
                if levels[y2][x2] - levels[y][x] <= 1:
                    visited.add((y2,x2))
                    queue.append((dist + 1, (y2,x2)))
                        
    return 10000

grid = open('12/input.txt').read().splitlines()
a_starts = sum([[(y,x) for x,c in enumerate(row) if c == 'a'] for y,row in enumerate(grid)], [])
levels = [[[0,25]['SE'.find(c)] if c.isupper() else ord(c)-97 for c in row] for row in grid]
start = max([[(y,x) for x,c in enumerate(row) if c == 'S'] for y,row in enumerate(grid)])[0]
end = max([[(y,x) for x,c in enumerate(row) if c == 'E'] for y,row in enumerate(grid)])[0]

print(bfs(grid, start, end, levels), min(bfs(grid, a_start, end, levels) for a_start in a_starts))

# 19 lines