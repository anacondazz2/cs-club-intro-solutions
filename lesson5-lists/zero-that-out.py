nums=[]
for i in range(int(input())):
    num = int(input())
    if num > 0:
        nums.append(num)
    else: nums.pop(-1)
print(sum(nums))
