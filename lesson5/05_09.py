# Bài 09: Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
my_tuple = (1,3,1.2,3.13,123)
sum_tuple = 0
max_tuple = my_tuple[0]
for ele in my_tuple:
    sum_tuple += ele
    if max_tuple < ele:
        max_tuple = ele
print("Sum = ",sum_tuple)
print("Max = ",max_tuple)
