# Bài 05: Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
my_list = [(2, 5, 6), (4, 1), (0, 0, 12), (2, 8, 9, 10), (4, 3, 7, 1)]
min_tuple = my_list[0][1]
for i in range(len(my_list)):   
    if min_tuple>my_list[i][1]:
        min_tuple = my_list[i][1]
        index = i
print(my_list[index])
