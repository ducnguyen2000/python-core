# Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
# Ví dụ:
#     Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#     Output: {'item1': 1150, 'item2': 300}
def new_dict(n):
    d = {}
    for i in range(len(n)):      
        for k,v in d.items():
            k = n[i]['item']
            v = n[i]['amount']
            d[k] = v
            if k in d:
                v += v
    return d
            
   
n = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(new_dict(n))

        
