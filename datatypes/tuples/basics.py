"""
Tuple
-----
Immutable , ordered. indexed , allows duplicates


"""
# thistuple = ("apple",89,6,"banana","apple",[678,'fghjk'])
# print(thistuple)
# tple = "orange",
# print(type(tple))
#
# print(thistuple[4])
# print(thistuple[5][-1])
#
# x = list(thistuple)
# print(x.append('asdfghj'))
# x[0]='grapes'
# print(tuple(x))
#
# thistuple = ("apple",89,6,"banana","apple",[678,'fghjk'])
# tupl = ("anand","alwin","albin")
# # print(thistuple+tupl)
# x = list(thistuple)
# x.extend(tupl)
# print(tuple(x))


# print(thistuple[0])
# Y = list(thistuple)
# Y[0] = 'grapes'
# print(tuple(Y))

# thistuple = ("apple", "banana", "cherry",[8,"rtyu",0])
# y = ("orange",)
# print(type(y))
# thistuple += y
#
# print(thistuple[3][0])

thistuple = ("apple", "banana", "cherry",[8,"rtyu",0])
# # x = list(thistuple)
# # y = x[3][::-1]
# # print(y)
# # # [(0,"apple",1,"banana")]
# index = 0
# for i in thistuple:
#     print(index,i)
#     index = index+1

#enumarate
thistuple = ("apple", "banana", "cherry",[8,"rtyu",0])
x = enumerate(thistuple)
print(list(x))

print(thistuple[3][::-1])
print(thistuple[3][0])

