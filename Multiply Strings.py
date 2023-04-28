# a = '2004'
# b = '30'
#
# dict1 = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
# sum1 = 0
# sum2 = 0
# for i in a:
#     sum1 = sum1*10 + dict1[i]
# for i in b:
#     sum2 = sum2*10 + dict1[i]
# res = sum1*sum2
# print(str(res))




num1 = '123'
num2 = '456'

res = [0] * (len(num1)+len(num2))
for i in range(len(num1)-1, -1, -1):
    carry = 0
    for j in range(len(num2)-1, -1, -1):
        current_value = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
        carry = (res[i+j+1]+current_value) // 10
        res[i+j+1] = (res[i+j+1]+current_value) % 10
    res[i] += carry
res = ''.join(map(str, res))
print(res)

print(ord('3')-ord('0'))