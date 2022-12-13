from functools import cmp_to_key

def compare(l,r):
    if isinstance(l, int) and isinstance(r, int):
        return l-r

    l = l if isinstance(l, list) else [l]
    r = r if isinstance(r, list) else [r]
    cmps = [c for c in map(compare, l, r) if c]
    return cmps[0] if cmps else len(l) - len(r)

packets = [eval(l) for l in open('13/input.txt').read().split('\n') if l != '']
print(sum([i+1 for i,c in enumerate(map(compare, packets[::2], packets[1::2])) if c < 0])) # task 1

packets = [0] + sorted(packets + [[[2]], [[6]]], key=cmp_to_key(compare))
print(packets.index([[2]]) * packets.index([[6]])) # task 2

# 12 lines