h = int(input())
w = h * 2 # width always = h * 2

halfLength = -1

for i in range(h):
    half = "" # half of line of asterisks
    mid = "" # whitespace in middle
    
    if i <= h // 2:
        halfLength += 2
    else:
        halfLength -= 2
    
    for _ in range(halfLength):
        half += '*'
    for _ in range(w - halfLength * 2):
        mid += ' '
    
    line = half + mid + half
    print(line)