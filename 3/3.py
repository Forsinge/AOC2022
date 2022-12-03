with open('3/input.txt') as f:
    lines, letters = f.read().split('\n'), ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    it, halve = iter(lines), lambda str: (str[:len(str)//2], str[len(str)//2:])
    print(sum(letters.find( min(set(a) & set(b) )) for a,b in map(halve, lines))) # task 1
    print(sum(letters.find( min((set(line) & set(next(it)) & set(next(it))) )) for line in it)) # task 2