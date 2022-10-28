n = int(input())
for _ in range(n):
    a = int(input())
    while a >= 10: # while a is double digit
        total = 0 # calculate total from a's digits
        while (a != 0):
            total += a % 10 # grabs a's last digit
            a //= 10 # deletes a's last digit
        a = total # set a to total. if a is still in double digits repeat the process
    print(a)