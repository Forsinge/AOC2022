nums = [[i,v] for i,v in enumerate(map(int, open("20/input.txt").readlines()))]
get_nums = lambda part: [[j,v] if part == 1 else [j, v * 811589153] for j,v in nums]
get_grove = lambda ns: ns[1000 % len(ns)] + ns[2000 % len(ns)] + ns[3000 % len(ns)]

def mix(nums, n):
    for _ in range(n):
        for l in range(len(nums)):
            i = next((j for j, num in enumerate(nums) if num[0] == l), None)
            (o,v), size = nums.pop(i), len(nums)
            ii = (i + v) % size
            ii = ii if 0 < ii < size or v == 0 else ii ^ size
            nums = nums[:ii] + [[o,v]] + nums[ii:]
    return nums

p1 = [l[1] for l in mix(get_nums(1), 1)]
p2 = [l[1] for l in mix(get_nums(2), 10)]
z1,z2 = p1.index(0), p2.index(0)
p1, p2 = p1[z1:] + p1[:z1], p2[z2:] + p2[:z2]
print(get_grove(p1), get_grove(p2))

# 17 lines