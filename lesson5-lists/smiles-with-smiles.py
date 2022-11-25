adjAmount=int(input())
nounAmount=int(input())
adjs=[]
nouns=[]
for i in range(adjAmount):
    adjs.append(input())
for j in range(nounAmount):
    nouns.append(input())
for adj in adjs:
    for noun in nouns:
        print(f"{adj} as {noun}")
