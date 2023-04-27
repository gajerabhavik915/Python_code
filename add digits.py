a = 38
b = 0
while len(str(a)) != 1:
    for i in str(a):
        b += int(i)
    a = b
    b = 0

print(a)
#
# print(5654//10)