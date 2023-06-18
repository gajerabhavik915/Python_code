#
# # list1 = [4,6,9,1,2,13,5,7]
import heapq
#
# list1  = [4,5,2,1,6,9,81,23,12,5,6,44,88,55]
# k = 8
#
# # list1 = [3,2,1,5,6,4]
# length = len(list1)
# checking = length - k
# last = length - 1
#
# def Quick_sort(l, first, last):
#     pivot = list1[last]
#     left = first
#     right = last - 1
#     while left <= right:
#         if list1[left] <= pivot:
#             left += 1
#         elif list1[right] >= pivot:
#             right -= 1
#         else:
#             list1[left], list1[right] = list1[right], list1[left]
#     else:
#         list1[left], list1[last] = pivot, list1[left]
#         print(right,list1)
#     return right, left
#
#
# def Quick1(list1, first, last):
#     if first < last:
#         rig,lef = Quick_sort(list1, first, last)
#         if rig > checking or lef > checking:
#             Quick1(list1, first, rig)
#         else:
#             Quick1(list1, rig+2, last)
#
# Quick1(list1, 0, last)
# print(list1)
# print(list1[checking])


minheap = []
nums = [2,1,3,5,6,8]
k = 6
def findKthLargest(nums, k):
    count = 0
    for num in nums:
        heapq.heappush(minheap,num)
        # print(minheap)
        count +=1
        if count > k:
            (heapq.heappop(minheap))
            # print(minheap)
    return minheap[0]

print(findKthLargest(nums, k))

def heapsort(nums, k):
    len1 = len(nums)
    if k > len1//2 and k != len1:
        k = len1-k
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappop(nums)
            print(nums)
        return nums[0]
    elif k == len1:
        heapq.heapify(nums)
        return (heapq.heappop(nums))

    else:
        heapq._heapify_max(nums)
        print(nums)
        for i in range(k-1):
            heapq.heappop(nums)
            (heapq._heapify_max(nums))
            # print(nums)
        return nums[0]

print(heapsort(nums, k))


