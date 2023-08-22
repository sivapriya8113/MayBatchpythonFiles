str1 = input("enter the string1:")
str2 = input("enter the string2:")
# convert both the strings into lowercase
str3 = str1.lower()
str4 = str2.lower()
# check if length is same
if(len(str3) == len(str4)):
    # sort the strings
    sorted_str1 = sorted(str3)
    print(sorted_str1)
    sorted_str2 = sorted(str4)
    print(sorted_str2)
    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")

# Rare care
# Earth Heart
