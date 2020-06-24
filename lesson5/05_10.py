# Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#     Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
my_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
ele = ''

for i in range(len(my_list)):
    ele = my_list[i].split('.')
    my_list[i] = ele[-1]   
print(my_list)

