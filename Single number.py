a = [2,3,4,3,4,5]

dict1 = {}
for i in a:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] += 1

for key, value in dict1.items():
    if value == 1:
        print(key)
        break

print(dict1)