import math

a = int(input())
b = int(input())
c = int(input())

ans = 0
badges = int(a / b)
ans += badges * c
leftoverPaint = a - badges * b
ans += leftoverPaint

print(ans)