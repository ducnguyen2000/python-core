# Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.

import random

my_list = random.sample(range(1000), 10)
new_list = [random.choice(my_list) for i in range(5)]
print(my_list)
print(new_list)