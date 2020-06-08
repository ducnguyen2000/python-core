s = input("Enter your string: ")
new_str = ""
for i in range(len(s)):
    if s[i].lower() == s[0].lower():
        new_str = s.replace(s[i],"$")

print("New string: ",new_str)
   