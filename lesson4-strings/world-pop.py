p=float(input())
y=int(input())
n=int(input())
x=int(input())

for i in range(x-y): # x-y gives the amount of years
  n*=1+(p)*0.01 # add the percentage (in decimal form) to the current population

print(int(n+0.5)) # the answer must be an answer (also: since int() always rounds down, adding 0.5 will make rounding possible)