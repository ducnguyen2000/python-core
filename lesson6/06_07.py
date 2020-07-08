# Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
# Ví dụ:
#     dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#     keys = ["name", "salary"]
#     Output: {'name': 'Kelly', 'salary': 8000}

def new_dict(n,key):
    result = {}
    for k,v in n.items():
        if k in key:
            result[k] = v
    return result
sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
print(new_dict(sampleDict, keys))