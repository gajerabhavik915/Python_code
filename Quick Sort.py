
# l = [4,6,9,1,2,13,5,7]

l = [4,6,5,1,2]
length = len(l)
# # pivot = l[length - 1]
# left = 0
right = length - 2

def Quick_sort(l, left, right):
    pivot = right+1
    while left <= right:
        if l[left] <= l[pivot]:
            left += 1
        elif l[right] >= l[pivot]:
            right -= 1
        else:
            l[left], l[right] = l[right], l[left]
    else:
        l[left], l[pivot] = l[pivot], l[left]
        return right


def Quick1(l,left, right):
    if left < right:
        p = Quick_sort(l,0, len(l) - 2)
        Quick_sort(l,left,p-1)
        Quick_sort(l, p+1, len(l) - 2)

list = Quick1(l,0,right)
print(list)



