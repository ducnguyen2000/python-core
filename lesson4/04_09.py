# Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
import random
a,b = [],[]
for i in range(3):
    a.append(random.sample(range(100),3))
    b.append(random.sample(range(100),3))
c = [[0,0,0],[0,0,0],[0,0,0]]
sum = 0
for i in range(3):
    for j in range(3):
        for k in range(3): 
            sum += a[i][k]*b[k][j]
        c[i][j] = sum
print("Matrix a: ",a)
print("Matrix b: ",b)
print("{a} * {b}".format(a=a,b=b))
print("Result: ",c)
