# Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list. 
#         Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.

my_list = [1, 1, "Hello", 2, 3, 2, 2, 1, "Hello"]
max_count = count = 0
highest_char = ''
for i in range(len(my_list)):
    count = my_list.count(my_list[i]) 
    if count > max_count:
        max_count = count
        highest_char = my_list[i]
print("Char has highest frequency :",highest_char)