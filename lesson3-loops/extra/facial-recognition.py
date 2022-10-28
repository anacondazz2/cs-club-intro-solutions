n = int(input())

count = 0

for _ in range(n):
    a = input()
    if a == "face":
        count += 1
        
print(count)