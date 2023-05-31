# stack is already implemented
# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)


# Function should pop an element from stack
def pop(arr):
    arr.pop()


# function should return 1/0 or True/False
def isFull(n, arr):
    if n == len(arr):
        return True
    else:
        return False


# function should return 1/0 or True/False
def isEmpty(arr):
    return False if arr else True


# function should return minimum element from the stack
def getMin(n, arr):
    if n == 1:
        return arr[0]
    a = arr[0]
    for i in arr[1:]:
        if a > i:
            a = i

    return a

