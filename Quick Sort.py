
# list1 = [4,6,9,1,2,13,5,7]
list1 = [4,5,2,1,6,9,81,23,12,5,6,44,88,55]


# list1 = [4,6,5,1,2]
length = len(list1)
last = length - 1

def Quick_sort(l, first, last):
    pivot = list1[last]
    left = first
    right = last - 1
    while left <= right:
        if list1[left] <= pivot:
            left += 1
        elif list1[right] > pivot:
            right -= 1
        else:
            list1[left], list1[right] = list1[right], list1[left]
    else:
        list1[left], list1[last] = pivot, list1[left]
        print(right,list1)
    return right



def Quick1(list1, first, last):
    if first < last:
        rig = Quick_sort(list1, first, last)
        Quick1(list1, first, rig)
        Quick1(list1, rig+2, last)

Quick1(list1, 0, last)
print(list1)


