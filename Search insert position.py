a = [7,9,10,12,14,17,18,19,20,22,24,25,30]


def searchInsert(nums):
    tar = 31
    leng = len(a)

    if a[len(a)-1] < tar:
        return leng
    elif a[len(a)-1] == tar:
        return leng - 1
    elif a[0] >= tar:
        return 0


    else:
        left, right = 0, leng-1
        while right - left != 1:
            half = (left+right)//2
            if a[half] < tar:
                left = half
            elif a[half] > tar:
                right = half
            else:
                return half
        return left + 1

print(searchInsert(a))