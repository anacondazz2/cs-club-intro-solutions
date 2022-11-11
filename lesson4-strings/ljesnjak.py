# NOTE: You will need to copy the special characters from the problem to use them. e.g. č
word = input()
word = word.replace("c=","č")
word = word.replace("c-","ć")
word = word.replace("dz=","ž") # first character is removed to allow the len() to count this as one character instead of two
word = word.replace("d-","đ")
word = word.replace("lj","j")
word = word.replace("nj","j")
word = word.replace("s=","š")
word = word.replace("z=","ž")

print(len(word))


