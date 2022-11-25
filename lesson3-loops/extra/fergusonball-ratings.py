n = int(input())

over40 = 0

for _ in range(n):
    a = int(input())
    b = int(input())
    stars = 5 * a - 3 * b
    if stars > 40:
        over40 += 1

print(over40, end="")
if (over40 == n):
    print('+')