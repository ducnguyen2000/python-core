# Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.

my_list = [1, 2, 3, 4, "Hello", "python", 2020, "World"]
print("Original list: ",my_list)
print("The length of original list: ",len(my_list))
list_len = int(input(f"Enter new list length in range {len(my_list)}: "))

if list_len<=len(my_list):
    list_1 = my_list[0:list_len]
    list_2 = my_list[list_len:len(my_list)]
    print("List 1: ",list_1)
    print("List 2: ",list_2)
else:
    print("Input out of range!")


