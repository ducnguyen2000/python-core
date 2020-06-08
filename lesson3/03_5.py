s = input("Enter your string: ")
min_ord = ord(s[0])
max_ord = ord(s[0])
for i in range(len(s)):
    if min_ord > ord(s[i]):
        min_ord = ord(s[i])
    if max_ord < ord(s[i]):
        max_ord = ord(s[i])

print("The largest character: ", chr(max_ord))
print("The smallest character: ", chr(min_ord))