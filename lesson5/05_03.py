# Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple
my_list = [1,3,2,"Hello",(2,4,45,6)]
count = 0
for ele in my_list:
    if type(ele) is tuple:
        break
    count += 1
print(count)