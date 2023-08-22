# def reverse(s):
#     str = ""
#     for i in s:
#         str = i+str
#         print(str)
#     return str
#
#
# s = "Python"
# print(str)
# print(reverse(s))
#
def reverse(string):
    string = [string[i] for i in range(len(string)-1,-1,-1)]
    print(string)
    print(s)
    x = "".join(string)
    if x==s:
        print("palindrome ")
    else:
        print("not palindrome")
    return x
s = input("enter the string:")
print(reverse(s))



def palindrome(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    print(str1)
    if s==str1:
        print("palindrome")
    else:
        print("not palindrome")
s = input("enter the string:")
palindrome(s)


#
# def find_first_missing_positive(nums):
#     i = 0
#     n = len(nums)
#
#     # Cyclic sort
#     while i < n:
#         num = nums[i]
#         if 0 < num <= n and num != nums[num - 1]:
#             nums[i], nums[num - 1] = nums[num - 1], nums[i]
#         else:
#             i += 1
#
#     # Find first missing positive integer
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
#
#     # All numbers from 1 to n are present
#     return n + 1
# print(find_first_missing_positive([1,2,0,4]))