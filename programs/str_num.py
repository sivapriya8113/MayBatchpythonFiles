"""
str = "123" to 123
"""
str1 = "123"
result = 0
for i in str1:
    digits = ord(i) - ord('0') #convert character to numerical value #1 , 2
    # print(digits)
    result = result*10+digits
    print(result)
    print(type(result))

# print(ord('A'))
# print(ord('1'))
# print(ord('2'))
# print(ord('0'))