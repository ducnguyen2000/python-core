# Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
def no_dup(n):
    result = {}
    for k,v in n.items():
        if v not in result.values():
            result[k] = v
    return result

my_dict = {1: 1, 3: 10, 2: 20, 5: "Hello", 4: "python", 6: 10}
print(no_dup(my_dict))
                
    


