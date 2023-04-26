a = [1,1,2,3,3,5,6,6,8,9,9,10]

limit = len(a)
x = 0
y = 1
count = 0
while x < limit and y < limit:
    if a[x] == a[y]:
        a[y] = '_'
        y += 1
        count += 1

    elif a[x] < a[y]:
        if y-x == 1:
            x += 1
            y += 1
        else:
            a[x+1], a[y] = a[y], '_'
            x += 1
            y += 1


print(a)
print(count)