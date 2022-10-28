print("Ready")
a = input()
while (a != "  "):
    if "b" in a and "d" in a:
        print("Mirrored pair")
    elif "q" in a and "p" in a:
        print("Mirrored pair")
    else:
        print("Ordinary pair")

    a = input() # grab the next line of input after each loop