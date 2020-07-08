# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
def is_perfect(n):
    sum_n = 0   
    for i in range(1,n):
        if n%i == 0:
            sum_n += i
    if sum_n == n:
        return True
    else:
        return False

print(is_perfect(7))
