# Bài 08: Cho list các số nguyên dương A.
#         Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
import random
list_len = int(input("Enter the length: "))
a = []
for i in range(list_len):
    a.append(random.randint(0,100))

count = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            count += 1
print(a)
print("Number of elements when a[i] > a[j] and i < j: ",count)