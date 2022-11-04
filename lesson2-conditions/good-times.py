t = int(input())
def convert(time,offset):
    x = time + offset
    if x < 0:
        x += 2400
    if x >= 2400:
        x -= 2400
    if x % 100 > 60:
        temp = x % 100
        x -= temp
        x += 100
        x += temp % 60
    return x
print(str(t) + " in Ottawa")
v = convert(t,-300)
print(str(v) + " in Victoria")
e = convert(t,-200)
print(str(e) + " in Edmonton")
w = convert(t,-100)
print(str(w)," in Winnipeg")
print(str(t) + " in Toronto")
h = convert(t,100)
print(str(h) + " in Halifax")
s = convert(t,130)
print(str(s) + " in St. John's")
