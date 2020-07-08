
# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
def count_upper_lower(s):
    c_u = 0
    c_l = 0
    for i in s:
        if i.isupper():
            c_u += 1
        elif i.islower():
            c_l += 1
        
    return c_u, c_l
print(count_upper_lower("Hello WOrld!"))