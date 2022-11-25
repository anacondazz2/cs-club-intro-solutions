instructions=[]
first=True
while True:
    x = input()
    if x == "SCHOOL": break
    if first:
        x = "LEFT" if x == "R" else "RIGHT"
        instructions.insert(0,["HOME",x])
        first = False
    else:
        y = input()
        y = "LEFT" if y == "R" else "RIGHT"
        instructions.insert(0,[x,y])
for i in range(len(instructions)):
    toPrint="Turn {} {}{} {}{}.".format(instructions[i][1],"onto" if instructions[i][0] != "HOME" else "into"," your" if instructions[i][0] == "HOME" else "",instructions[i][0]," street" if instructions[i][0] != "HOME" else "")
    print(toPrint)