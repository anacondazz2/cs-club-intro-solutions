phrase = input()
letters = "IOSHZXN"
allowed = True
for letter in phrase:
    if letter not in letters:
        allowed = False
        break

if allowed:
    print("YES")
else:
    print("NO")