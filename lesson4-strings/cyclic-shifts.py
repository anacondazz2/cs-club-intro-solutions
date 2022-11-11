phrase = input()
string = input()
contains = False
for i in range(len(string)):
  x = string[i:]+string[:i]
  if x in phrase:
    contains = True

if contains:
  print('yes')
else:
  print('no')
    