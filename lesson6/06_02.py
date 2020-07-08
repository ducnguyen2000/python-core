# Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
def sort_dict(n):
    l = []
    for k,v in n.items():       
        l.append([k,v])
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i][0] > l[j][0]:
                l[i][0],l[j][0] = l[j][0],l[i][0]
    return dict(l)

my_dict = {1: 1, 3: 10, 2: 20, 5: "Hello", 4: "python"}

print(sort_dict(my_dict))
