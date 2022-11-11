verb = input()
object = input()

phrase=verb+"-tu"

if object.endswith("e"):
  phrase += " la "
elif object.endswith("s"):
  phrase += " les "
else:
  phrase += " le "

phrase += object + " ?"

print(phrase)