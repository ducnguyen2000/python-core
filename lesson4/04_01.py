# Bài 01: Viết chương trình tính tổng, tích của các phần tử trong một list.

my_list = [1,2,3,4,5]
tong = 0
tich = 1

for i in my_list:
    tong += i
    tich *= i
print("Tong cua list: ", tong)
print("Tich cua list: ", tich)
