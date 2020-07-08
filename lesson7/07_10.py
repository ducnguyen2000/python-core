# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
def odd_digit(n):
    if n == 0:
        return 0
    if (n%10)%2 != 0:
        return 1 + odd_digit(int(n/10))
    else:
        return odd_digit(int(n/10))

n = 12
print(odd_digit(n))