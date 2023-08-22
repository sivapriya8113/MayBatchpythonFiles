"""
dict comprehension:


dictionary = {key:value for vars in iterable}


"""
#
square_dict = {}
for num in range(1,11):
    square_dict[num] = num*num
print(square_dict)
#
#dict_comprehension
square_dict = {num:num*num for num in range(1,11) }
print(square_dict)


old_price = {'milk': 1.02, "coffee": 2.5, "bread": 2.5}
dollar_to_pound = 0.76
new_price = {key: value * dollar_to_pound for (key, value) in old_price.items()}
print(new_price)

first_dict = {'jack': 38, 'jin': 48, 'guido': 57, 'john': 89}
even_dict = {k: v for (k, v) in first_dict.items() if v % 2 == 0}
print(even_dict)
#
keys = ['a','b','c','d','e','f']
for i in keys:
    for j in i:
        print(i,j)











values = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(keys,values)}
print(mydict)

dict = {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


even_odd = {k: ('even' if k % 2 == 0 else  'odd'  ) for k in range(1, 11)}
print(even_odd)
