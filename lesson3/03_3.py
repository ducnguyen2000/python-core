s = input("Enter your string: ")
new_s = ""
index = 0
for word in s:
    if index%2 != 0:
        word = ""
        new_s += word
    else:
        new_s += word
    index += 1
print("The new string: ",new_s)