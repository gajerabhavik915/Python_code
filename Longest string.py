# str = ["flower","flow","flight", "florida", "flora", ""]
str = ['flower']

min_len = len(str[0])
index1 = 0


for index, i in enumerate(str):
    if len(i) < min_len:
        min_len = len(i)
        index1 = index

print(min_len)
print(index1)

res = str[index1] + ""

for i in str:
    for a in range(len(res)):
        if i[a] == res[a]:
            continue
        else:
            res = res[:a]
            print(res)
            break


print(res)
# print(min_len)
# print(index1)