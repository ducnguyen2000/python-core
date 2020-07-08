# Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
#         Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
def fifth_value(n):
    if len(n)< 3 :
        return False
    for k,v in n.items():
        if len(v) < 5:
            return False
        else:           
            print(v[4])



my_dict = {1: [1,2,"Hello","python",3,7,8], 2:[2,0,1,4,"World"], 3: [1,3,2,4,5], 4: ["a",2,41,2,3,6]}
print(fifth_value(my_dict))