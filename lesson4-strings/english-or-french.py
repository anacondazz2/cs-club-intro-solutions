n = int(input())
phrase = ""

for i in range(n):
  phrase += input()
  
s = phrase.lower().count("s")
t = phrase.lower().count("t")

if t > s:
  print("English")
else:
  print("French")