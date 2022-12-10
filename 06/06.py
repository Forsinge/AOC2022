message = open('06/input.txt').read()

print([len(set(message[i- 4:i])) ==  4 for i in range( 4, len(message))].index(True)+ 4) # part 1
print([len(set(message[i-14:i])) == 14 for i in range(14, len(message))].index(True)+14) # part 2

# 3 lines