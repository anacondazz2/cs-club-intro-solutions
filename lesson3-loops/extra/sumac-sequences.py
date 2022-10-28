cur = int(input())
nxt = int(input())

count = 2

while (cur >= nxt):
    temp = nxt
    nxt = cur - nxt
    cur = temp
    count += 1
    # print(cur, nxt)
    
print(count)