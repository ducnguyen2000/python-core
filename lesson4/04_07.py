# Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
import random
list_1,list_2 = [],[]
list_1.append(random.sample(range(5),5))
list_2.append(random.sample(range(5),5))
print("List 1: ",list_1)
print("List 2: ",list_2)

index = 0
while index < len(list_1):
    if list_1[index] in list_2:
        print("2 list have the same element")
    else:
        index += 1



    
    