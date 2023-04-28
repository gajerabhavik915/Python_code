a = 26
min = 0
max = a
while max-min > 1:
    median = (min+max)//2
    if median**2 > a:
        max = median
    else:
        min = median
print(min)