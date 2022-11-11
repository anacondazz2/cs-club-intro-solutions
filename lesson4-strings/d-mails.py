n = int(input())

m1 = "elpsycongroo"
m2 = "tuturu"
m3 = "superhacker"
m4 = "myfork"

for i in range(n):
  phrase = input()
  
  y = ""
  cnt = 0
  for c in range(len(phrase)):
    x = phrase[c]
    if x == m1[cnt]:
      if cnt + 1 < len(m1):
        cnt+=1
    
      y+=x

  z = ""
  cnt = 0
  for c in range(len(phrase)):
    x = phrase[c]
    if x == m2[cnt]:
      if cnt + 1 < len(m2):
        cnt+=1
      z+=x

  v = ""
  cnt = 0
  for c in range(len(phrase)):
    x = phrase[c]
    if x == m3[cnt]:
      if cnt + 1 < len(m3):
        cnt+=1
      v+=x

  b = ""
  cnt = 0
  for c in range(len(phrase)):
    x = phrase[c]
    if x == m4[cnt]:
      if cnt + 1 < len(m4):
        cnt+=1
      b+=x

  toPrint= ""
  if m1 in y:
    toPrint+="Okabe"
  if m2 in z:
    if len(toPrint) != 0:
      toPrint += " or "
    toPrint+="Mayuri"
  if m3 in v:
    if len(toPrint) != 0:
      toPrint += " or "
    toPrint+="Daru"
  if m4 in b:
    if len(toPrint) != 0:
      toPrint += " or "
    toPrint+="Kurisu"
  if m1 not in y and m2 not in z and m3 not in v and m4 not in b:
    toPrint = "SERN spy!"
  print(toPrint)