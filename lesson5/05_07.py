# Bài 07: Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
tuple_1 = (1,2,"Hello",6,3,9)
tuple_2 = (10,"world!",11,9)
for ele in tuple_1:
    if ele in tuple_2:
        print("True")
        break
    if ele == tuple_1[-1] and ele not in tuple_2:
        print("False")

    
