w = int(input())
h = int(input())

isZero = None
for r in range(h): # r stands for row
    # figure out whether the starting number is 0 or 1 depending on row #
    if (r % 2 == 0): # if r is even
        isZero = True 
    else:
        isZero = False
        
    for c in range(w): # c stands for column
        if isZero:
            print(0, end="")
        else:
            print(1, end="")
        isZero = not isZero # flip the boolean
    print()