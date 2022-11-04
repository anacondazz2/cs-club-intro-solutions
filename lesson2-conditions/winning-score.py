a=0
b=0
a3=int(input())
a2=int(input())
a1=int(input())
b3=int(input())
b2=int(input())
b1=int(input())
a3 *= 3
a2 *= 2
b3 *= 3
b2 *=2

b = b3 + b2 + b1
a = a3 + a2 + a1
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('T')
