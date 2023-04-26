
# Solved through sliding window

nums = [3,3,3,2,4,6,3,5,8]

val = 3
a = 0
b = 1
limit = len(nums)
while b < limit :
    if nums[a] == val:
        # nums[a] = '_'
        nums[a], nums[b] = nums[b], '_'
        b += 1
    elif nums[b] == val:
        nums[b] = '_'
        b += 1
    else:
        if b-a == 1:
            a += 1
            b += 1
        else:
            nums[a+1], nums[b] = nums[b], '_'
            a += 1
            b += 1

print(nums)
