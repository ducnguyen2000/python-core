# Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
s = input("Enter your input: ")
my_list = [1, 2, 3, 4, 5, "Hello", "python"]
new_list = []
new_ele = ''
for i in my_list:
    new_ele = str(i) + s 
    new_list.append(new_ele)
print("The new list: ", new_list)