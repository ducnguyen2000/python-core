# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
def change_upper_lower(s):
    new_s = ''
    for i in s:
        if i.isupper() == True:
            new_s += i.lower()
        elif i.islower() == True:
            new_s += i.upper()
        else:
            new_s += i
    return new_s
       
s = "Hello wORld"
print(change_upper_lower(s))