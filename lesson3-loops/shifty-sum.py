n = int(input())
k = int(input())

total = 0
for x in range(k + 1):
    a = n * 10 ** x
    total += a
    
print(total)