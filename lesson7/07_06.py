# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
def is_pangram(s):
    l = [chr(x) for x in range(ord('a'),ord('z')+1)]
    for c in range(ord('a'),ord('z')+1):
        if chr(c) not in (s.lower()):
            return False
    return True
s = "Waltz, bad nymph, for quick jigs vex."
print(is_pangram(s))