"""
1.Reverse a number
  num = 4570

2. To check whther  a number is amstrong number

3. To remove the duplicates from a each word in a string
   str = " Let's google the pineapple photo "
   o/p: "Let's gole the pineale phot"

"""

# str = " Let's google the pineapple photo "
# str1 = str.split()
# re_words = []
# for word in str1:
#         word = word[::-1]
#         re_words.append(word)
# print(re_words)
# print(" ".join(re_words))
# # print(re_words)

str = '23456787654329'
num = []
even = []
odd = []
for i in str:
    num.append(int(i))
for j in num:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
odd.sort()
even.sort(reverse=True)
print(odd)
print(even)
even_int = [str[x] for x in even]
odd_int = [str[y] for y in odd]
print(odd_int)
print((even_int))
lastnum = odd_int+even_int
print(''.join(lastnum))



# num = 4570
# reverse = 0
# while num > 0:
#     reminder = num % 10
#     reverse = reverse * 10 + reminder
#     num = num // 10
# print(reverse)
