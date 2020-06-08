s = input("Enter your string: ")
new_s = ""
if len(s) >= 2:
    new_s += s[0] + s[1] + s[-2] + s[-1]
else:
    new_s += ""

print("New string: ", new_s)
