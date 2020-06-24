# Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
#     Sau đó, unpack các phần tử trong một tuple.
my_tuple = (1,2,"Hello",7.12,["World!",159] )
for i in range(len(my_tuple)):
    print(f"Index {i} = {my_tuple[i]}")


