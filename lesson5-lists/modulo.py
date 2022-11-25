nums = []
for i in range(10):
    x = int(input())
    y = x % 42
    if y not in nums:
        nums.append(y)
print(len(nums))
