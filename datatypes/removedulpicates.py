"""
Write a python code to remove all the repeating letters
 from  each words of a given sentence.
Eg:
   			i/p:Let’s google the pineapple
 			o/p:Let’s gole the pineal
"""
str1 = "Let’s google the pineapple"
str2 = str1.split()
str3 = []
# print(str2)
for i in str2:
    # print(i)
    k = ""
    for j in i:
        # print(j)
        if j in k:
            continue
        else:
            k = k+j
    print(k)
    str3.append(k)
    print(str3)
print(" ".join(str3))
