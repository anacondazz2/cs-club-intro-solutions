count = int(input())
votes = input()
b = votes.count("B")
a = votes.count("A")

if a > b :print("A")
elif b > a:print("B")
else:print("Tie")
