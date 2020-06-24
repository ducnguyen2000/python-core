# Bài 02: Viết chương trình đảo ngược một tuple.
my_tuple = (1,2,3,4,7,8,"Hello")
reverse_tuple = []
for i in range(len(my_tuple)-1,-1,-1):
    reverse_tuple.append(my_tuple[i])

print(tuple(reverse_tuple))