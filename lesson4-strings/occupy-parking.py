n=int(input())
yester=input()
tod=input()

occupied=0
for x in range(len(yester)):
    if yester[x] == tod[x] == 'C':
        occupied+=1
print(occupied)