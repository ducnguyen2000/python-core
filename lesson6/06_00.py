# Bài 00: Viết chương trình tính tích các phần tử trong một dict
def mul_dict(n):
    mul = 1
    for value in n.values():
        mul *= value
    return mul

my_dict = {1: 1, 2: 10, 3: 20}
print(mul_dict(my_dict))
