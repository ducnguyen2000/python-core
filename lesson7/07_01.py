# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào
def max_min(*numbers):
    return max(*numbers), min(*numbers)

print(max_min(1,3,2,45,0,-10))