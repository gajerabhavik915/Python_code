# a = [1,2,3,4,5,6,7,8]
a = [-1,-100,3,99]
#[99,3,-100,-1]

k = 2
length = len(a) #4

a = a[-k:] + a[:len(a)-k]
print(a)

# method -2

for i in range(k):
    s = a.pop()
    print(s)
    a.insert(0, s)

print(a)

# method -3

a = [1,2,3,4,5,6,7,8]
k = 11 #3
# [8,7,6,5,4,3,2,1]
# [6,7,8,1,2,3,4,5]

k = k%len(a) if k > len(a) else k
first, last = 0, len(a)-1
while first < last:
    a[first], a[last] = a[last], a[first]
    first, last = first + 1, last -1


first, last = 0,k-1
while first < last:
    a[first], a[last] = a[last], a[first]
    first, last = first+1, last-1

first, last = k, len(a)-1
while first < last:
    a[first], a[last] = a[last], a[first]
    first, last = first + 1, last - 1

print(a)
