# Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple

a = [1,23,14,"Hello"]
if type(a) is list:
    print(tuple(a))
elif type(a) is tuple:
    print(list(a))
