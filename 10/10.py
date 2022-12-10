inp, xs, pxs = open('10/input.txt').read().replace('addx', '0\n').replace('noop', '0'), [1], [1]
[(xs.append(xs[-1]+int(v)), pxs.append(xs[-1]-(i+1)%40) ) for i,v in enumerate(inp.split('\n'))]

print(sum([xs[i-1]*i for i in range(len(xs))][20::40])) # task 1
print('\n'.join([''.join([' █'[abs(px)<2] for px in pxs[l:l+40]]) for l in range(0,240,40)])) # task 2

# 4 lines