
l = [4,6,9,1,2,13,5,7]

length = len(l)
pivot = l[length - 1]
left = 0
right = length - 2

def Quick_sort(l, pivot, left, right):
    while left < right:
        if l[left] <= l[pivot]:
            left += 1
        elif l[right] >= l[pivot]:
            right -= 1
        else:
            l[left], l[right] =  l[right], l[left]
    else:
        l[left], l[pivot] = l[pivot], l[left]
        print(l)
        return True

# list = Quick_sort(l,pivot,left, right)



