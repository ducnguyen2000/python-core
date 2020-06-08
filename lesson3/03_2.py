s = input("Enter your string: ")
print("The number input can only in this range 0 to {} ".format(len(s)-1))
n = int(input("Enter the positive number: "))
new_s = ""
if n >= 0 and n <= len(s):
    for i in range(len(s)):
        if i == n:
            new_s = s.replace(s[i], "",1)
            break
else:
    print("Invalid input try again!")

print("The new string is: ",new_s)



