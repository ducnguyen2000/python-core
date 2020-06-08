n = int(input("Enter n: "))
sum = 0
for i in range(n):
    if i%3 == 0:
        sum += i
print("Sum of all number divisible by 3 less than n is: ", sum)

