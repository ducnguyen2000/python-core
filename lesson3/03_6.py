s = input("Enter your input: ")
new_s = ""

for word in s:
    if word == word.upper():
        new_s += word.lower()
    else:
        new_s += word.upper()
print("New string: ",new_s)