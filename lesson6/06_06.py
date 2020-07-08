# Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict
def  same_ele(d1,d2):
    for k,v in d1.items():
        if k in d2.keys() and v in d2.values():
            print(f"{k}: {v}")
d1 =  {1: 1, 2: 2, 3: 0}
d2 = {1:-1, 2: 2, 3: 0}
same_ele(d1,d2)
