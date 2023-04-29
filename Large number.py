a = []


res = ''
for i in range(len(a)):
    a1 = 0
    b = 1

    while b < len(a) and a1 < len(a):

        fir_pos = str(a[a1])
        sec_pos = str(a[b])
        if len(fir_pos) == len(sec_pos):
            if fir_pos[:1] < sec_pos[:1]:
                a1 += 1
            elif fir_pos[:1] == sec_pos[:1]:
                if fir_pos < sec_pos and sec_pos[-1] != 0:
                    a1 += 1
                else:
                    b += 1
            else:
                b += 1
        elif len(fir_pos) > len(sec_pos):   # 67 > 6
            if fir_pos[:1] < sec_pos[:1]:
                a1 += 1
            elif fir_pos[:1] == sec_pos[:1]:  # 6 == 6
                if fir_pos > sec_pos and fir_pos[-1] != 0:
                    a1 += 1
                else:
                    b += 1
            else:
                b += 1

        else:
            if fir_pos[:1] < sec_pos[:1]:
                a1 += 1
            elif fir_pos[:1] == sec_pos[:1]:
                if fir_pos < sec_pos and sec_pos[-1] != 0:
                    a1 += 1
                else:
                    b += 1
            else:
                b += 1
    res += str(a.pop(a1))
    # print(res)
    # break
print(res)




# 9954323522512319