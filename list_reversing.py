import builtins

l = [1, 2, 3, 4, 5, 6, 7]

# method - 1
# for i in l[::-1]:
#     print(i)


# method - 2
import time

start = time.perf_counter()
for a in range(((len(l)) // 2)):  # 0
    b = l[a]  # 1
    l[a] = l[(len(l) - 1 - a)]
    l[(len(l)) - 1 - a] = b
end = time.perf_counter()
print(l)
print(-start + end)

# method- 3
l1 = [1,2,3,4]
# import time
list = []
start1 = time.perf_counter()
for a in l1[::-1]:
    list.append(a)
    # print(a)
end1 = time.perf_counter()
print(list)
print(end - start)

