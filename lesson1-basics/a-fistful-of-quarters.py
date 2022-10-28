a = int(input()) * 4 # convert amount in dollars to num quarters
b = int(input()) 

needed = a - b

print(max(needed, 0))