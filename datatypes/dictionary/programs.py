keys = ['a','b','c','d','e','f']

first_value = [keys[i] for i in range(0,len(keys),2)]
second_value = [keys[j] for j in range(1,len(keys),2)]
print(dict(zip(first_value,second_value)))

new_dict = {keys[i]:keys[i+1] for i in range(0,len(keys),2)}
print(new_dict)