class Solution:
    def majorityElement(self, nums: [int]) -> int:
        len1 = len(nums) / 2
        dict1 = {}  # 3:1, 2:1
        count = 1
        for i in nums:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = count

        for element, count in dict1.items():
            if count > len1:
                return element





