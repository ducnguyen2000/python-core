# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy

def trifibo_incur(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    else:
        return trifibo_incur(n-1) + trifibo_incur(n-2) + trifibo_incur(n-3)
def trifibo(n):
    f = [0,1,1]
    if n < 3:
        return f[n]
    for i in range(3,n+1): 
        f.append(f[i-1] + f[i-2] + f[i-3])
    return f[n]
n = 10
print(trifibo_incur(n))
print(trifibo(n))
