# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h

def body_mass_index(m,h):
    return round((m/(h**2)),1)
def bmi_information(m, h):
    bmi = round((m/(h**2)),1)
    if bmi < 18.5:
        print("Gầy")
    elif bmi>= 18.5 and bmi < 24.9:
        print("Bình thường")
    else:
        print("Béo")

m = 70
h = 1.73
print(body_mass_index(m,h))
bmi_information(m,h)