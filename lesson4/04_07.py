# Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
import random
l1 = int(input("Enter length list 1: "))
l2 = int(input("Enter length list 2: "))
list_1,list_2 = [],[]
for i in range(l1):
    list_1.append(random.randint(0,100))
for j in range(l2):
    list_2.append(random.randint(0,100))

print("List 1: ",list_1)
print("List 2: ",list_2)

for x in list_1: 
    if x in list_2:
        print("2 list have the same element")
        break
    elif x not in list_2 and x == list_1[-1]:
        print("2 list have the different element")
    

    
    