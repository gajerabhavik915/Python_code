a = 27458
b = 0

# method 1
while len(str(a)) != 1:
    for i in str(a):
        b += int(i)
    a = b
    b = 0

print(a)

# method 2
while a >= 10:
    while a :
        b += (a % 10)
        a = a // 10
    # b += a
    a = b
    b = 0

print(a)


# method 3
def addDigits(num: int):
    sum = 0
    while num >= 10:
        sum += (num%10)
        num = num//10
    sum = sum + num
    num = sum
    return num if num < 10 else addDigits(num)

print(addDigits(a))
