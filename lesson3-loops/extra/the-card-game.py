n = int(input())

num_players = 0
too_young = 0

for _ in range(n):
    a = int(input())
    if a < 0:
        continue
    else:
        if a > 14:
            num_players += 1
        else:
            too_young += 1
        
if too_young > 0:
    if too_young == 1:
        print(f"1 person is too young to play.")
    else:
        print(f"{too_young} people are too young to play.")
if num_players < 12:
    print("There are not enough people to play.")
elif num_players > 12:
    print("There are too many people who want to play.")
else:
    print("Time to play!")