# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
def find_x(l,x):
    result = ''
    if x not in l:
        return -1
    for i in range(len(l)):
        if x == l[i]:
            result += str(i) + ' '
    return result
l = [1,2,4,4,2,3,5,6,1]
x = 1
print(find_x(l,x))