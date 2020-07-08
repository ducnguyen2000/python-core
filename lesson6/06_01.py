# Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
def dict_min_max(n):
    key_max = max(n.keys(), key = (lambda x: n[x]))
    key_min = min(n.keys(), key = (lambda x: n[x]))
    return key_max,key_min
my_dict = {1: 1, 2: 10, 3: 20}
print(dict_min_max(my_dict))