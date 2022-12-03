with open('3/input.txt') as f:
    lines, letters = f.read().split('\n'), ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    halves = [(s[:len(s)//2], s[len(s)//2:]) for s in lines]
    triples = [lines[i:i+3] for i in range(0, len(lines), 3)]
    print(sum(letters.find(min(set(a) & set(b))) for a,b in halves))  # task 1
    print(sum(letters.find(min(set(a) & set(b) & set(c))) for a,b,c in triples)) # task 2