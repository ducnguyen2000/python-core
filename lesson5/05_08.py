# Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
my_tuple = (1,1,1,1,1,1,2)
count = 0 
for i in range(len(my_tuple)-1):
    if my_tuple[i] != my_tuple[i+1]:
        count += 1
        break
if count == 0 :
    print("True")
else :
    print("False")

    