a = int(input())
b = int(input())
r = int(input())

days, total = 0, b

while total <= a:
    newInfected = 0
    for x in range(b):
        newInfected += r
    total += newInfected
    b = newInfected
    days += 1
    
print(days)