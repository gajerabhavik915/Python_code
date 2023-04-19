dic = {'name' : 'Bhavik', 'surname' : 'Gajera', 'age' : 20, 'location':'canada'}

# without comprehensive of dict.
dict1 = {}
for key, value in dic.items():
    # print(key)
    if key != 'age':
        dict1[key] = value

print(dict1)

# ---------------------------------------------------------------------------------
# with comprehensive

obj = {key:value for key,value in dic.items() if key != 'age'}
print(obj)

# sec example
l = [10,20,30,40,50,60]

obj = {key+1:value for key,value in enumerate(l)}
print(obj)