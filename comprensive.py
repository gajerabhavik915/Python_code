# print('this is list comprehensive')
#
#
# x,y,z,n = 1,1,1,2
#
#
# list1 = [x,y,z]
# a = [[0,0,list1] for list1 in range(x)]
# b = [[0,list1,0] for list1 in range(y)]
# c = [[list1,0,0] for list1 in range(z)]
# # a1 = [x1 for x1 in list1]
# # list = [[0,0,list1] for list1 in range(int(a1))]
# a1 = []
# (a1.extend(a))
# (a1.extend(b))
# (a1.extend(c))
# print(a1)
# a3 = []
# for a2 in a1:
#     b1 = 0
#     for aa1 in a2:
#         b1 = b1 + aa1
#     if b1 >= n or a2 in a3:
#         continue
#     else:
#         a3.append(a2)
#
# print(a3)
# [2,3,6,6,5]
# arr = [6,6,-2,3]
# arr = [1,-1,-2,0]
# arr = [-6,6,6,-7]
# arr = [27,27,27,2,-27,0]
n = 4
# min = arr[0]
# max = arr[1]
# if min < max:
#     pass
# else:
#     min,max = max,min
#
# if n > 2:
#     for i in arr[2:]:
#         if i > max:
#             min = max
#             max = i
#         elif i == max:
#             max = i
#         elif i < max and min < i and i>=0:
#             min = i
#         elif i < max and i < 0 and i > min or (min<0 and i> min):
#             min = i
#
# print(min)

# a = 0
# for i in arr:
#     if i > a:
#         a = i
#         # print(a)
#         continue
# print(a)
# b = arr[0]
#
#
# for i in arr:
#     if i < a and b < i:
#         b = i
#         # print(b)
#         continue
#     # elif i == a:
#
# print(b)

# arr = [2,3,6,6,5,7]
arr = [-7, -7, -7, -7, -6]
arr = list(arr)
a = -100
for i in arr:
    if i > a:
        a = i
        # print(a)
        continue
print(a)
b = 0
for i in arr:
    if i < b or i < 0:
        b = i
        # print(b)  

print(b)

for i in arr:
    if i < a and b < i:   #-7, -7, -7, -7, -6
        b = i
        # print(b)
        continue
print(b)
