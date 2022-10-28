a = int(input())
b = int(input())

ways = 0
for x in range(1, a + 1):
    for y in range(1, b + 1):
        if x + y == 10:
            ways += 1
if ways == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {ways} ways to get the sum 10.") # use f strings now on please