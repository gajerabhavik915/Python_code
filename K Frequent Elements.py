
# nums = [1,1,1,2,2,3,1,1,2,2,5,6,3,3]
nums=[1,2]

k = 1
dict1 = {}
# count = 1
pos = 0
l = len(nums)

if k ==1:
    while l > 0:
        if nums[pos] not in dict1.keys():
            dict1[nums[pos]] = 1
            pos += 1

        else:
            nums.pop(pos)
        l = l - 1




while l > 0 :
    if nums[pos] not in dict1.keys():
        dict1[nums[pos]] = 1
        nums.pop(pos)

    else:
        dict1[nums[pos]] = dict1[nums[pos]] + 1
        if dict1[nums[pos]] > k or dict1[nums[pos]] < k:
            nums.pop(pos)
        else:
            pos += 1
    l = l-1

print(nums)





# for j,i in enumerate(nums):
#     if i not in dict1.keys():
#         count = 1
#         dict1[i] = count
#         nums.pop(j)
#     elif i in dict1.keys():
#         count += 1
#         dict1[i] = count
#         if dict1[i] > k or dict1[i] < k:
#             nums.pop(j)




