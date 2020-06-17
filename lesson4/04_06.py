# Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
#         + Độ dài từ 2 trở lên
#         + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau

my_list = [1, 2, 2, "Hello", "!", "World", 5, 6, "Wow", "!python!"]
count = 0
for i in my_list:
    if type(i) is str and len(i) >= 2 and i[0].lower() == i[-1].lower():
        count += 1

print("Total: ", count)