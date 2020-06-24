# Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
s = input("Enter your sentence: ")
word = s.split()
longest = word[0]
for ele in word:
    if len(longest) < len(ele):
        longest = ele
print(longest)
