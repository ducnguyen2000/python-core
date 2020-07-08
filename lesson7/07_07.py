# Bài 07: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
def create_matrix(n, m): 
    l = []  
    for row in range(n):
        l_inner = []
        for column in range(m):
            l_inner.append(row*column)
        l.append(l_inner)
    return(l)
print(create_matrix(3,2))