a1 = [0,2,3,4,6,8,9]

output= []



a,b = 0,0
while b < len(a1) - 1:
    if a1[b+1] - a1[b] == 1:
        b += 1

    elif a1[b+1] - a1[b] != 1 and a1[a] == a1[b]:
        output.append(str(a1[a]))
        b += 1
        a = b

    else:
        output.append(str(a1[a])+'->'+str(a1[b]))
        b += 1
        a = b
if a1[a] == a1[b]:
    output.append(str(a1[a]))
else:
    output.append(str(a1[a]) + '->' + str(a1[b]))

print(output)