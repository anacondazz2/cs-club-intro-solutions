a = int(input())
b = int(input())
c = int(input())

# order of if statements is important

if (a + b + c) != 180:
    print("Error")
    # by checking this first, all elifs beneath guarantee the angles add up to 180
elif a == 60 and b == 60 and c == 60:
    print("Equilateral")
    # general rule of thumb is to first check the ifs where there is NO AMBIGUITY -
    # (a == 60 and b == 60 and c == 60) MUST be equilateral, but (a == b or a == c or b == c) could be either equilateral OR isosceles
elif a == b or a == c or b == c:
    print("Isosceles")
    # since equilaterals were checked above, all cases that reach this part of the code will not be equilateral
else:
    print("Scalene")
    # all cases that reach this part of the code must be scalene