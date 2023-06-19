# method - 1
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        count = 0
        res = 0

        for i in nums:
            if count == 0:
                res = i
            if i != res:
                count -= 1
            else:
                count += 1

        return res



# method - 2

# class Solution:
#     def majorityElement(self, nums: [int]) -> int:
#         len1 = len(nums) / 2
#         dict1 = {}  # 3:1, 2:1
#         count = 1
#         for i in nums:
#             if i in dict1:
#                 dict1[i] = dict1[i] + 1
#             else:
#                 dict1[i] = count
#
#         for element, count in dict1.items():
#             if count > len1:
#                 return element
nums = [1,2,2,4,2,3,3,3,3,3]
count1 = 1
res = nums[0]
for i in nums[1:]:
    if i != res:
        count1 -= 1
        if count1 == 0:
            res = i
            count1 += 1
    elif i == res:
        count1 += 1
    if count1 == 0:
        res = i
        count1 += 1




count = 0
res = 0
for i in nums:
    if count == 0:
        res = i
    if i != res:
        count -= 1
    else:
        count += 1
print(res)