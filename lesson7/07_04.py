# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
import math
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i < math.sqrt(n):
        if n%i == 0:
            return False
        i += 1
    return True
print(is_prime(9))