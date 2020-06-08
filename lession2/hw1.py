a = int(input("Enter a: "))
b = int(input("Enter b: "))

if (a > 0 and b < 0) or (a < 0 and b < 0 and a > b):
    for i in range(a - 1, b, -1):
        print(i, end =' ')
else:
    for i in range(a + 1, b):
        print(i, end = ' ')
