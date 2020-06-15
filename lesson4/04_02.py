# Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.

my_list = [1,2,3,4,5,10,20]
lmin = my_list[0]
lmax = my_list[0]
for i in range(len(my_list)):
    if my_list[i] < lmin:
        lmin = my_list[i]
    if my_list[i] > lmax:
        lmax = my_list[i]
print("Max in list: ", lmax)
print("Min in list: ", lmin)
