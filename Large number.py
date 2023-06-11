nums = [3,30,34,5,9]
#

output = ''
for i in range(len(nums)):
    first = 0
    sec = 1
    while first < len(nums) and sec < len(nums):
        str_fst = str(nums[first])
        str_sec = str(nums[sec])
        if len(str_fst) == len(str_sec):
            if str_fst[:1] > str_sec[:1]: #99, 88
                sec += 1
            elif str_fst[:1] == str_sec[:1]:
                if str_fst > str_sec:               # 22, 20   99909988 998899
                    sec += 1
                else:
                    first += 1
            else: #88, 90    #9088 #8890  #88 90
                first += 1


        elif len(str_fst) > len(str_sec): #22 #9
            if str_fst[:1] > str_sec[:1]: #99, 3
                sec += 1
            elif str_fst[:1] == str_sec[:1]:               # 99 9
                if nums[first]%10 == 0:   #90 9
                    first += 1
                else:                     #99 9
                    sec += 1
            else:
                first += 1


        else:  #2 99
            if str_fst[:1] > str_sec[:1]: #9 22
                sec += 1
            elif str_fst[:1] == str_sec[:1]: #9 99
                if nums[sec]%10 == 0:  #9 90
                    sec += 1
                else:                  #90 999
                    first += 1
            else: # 2 99
                first += 1
    val = nums.pop(first-1)
    print(val)



#
# res = ''
# for i in range(len(a)):
#     a1 = 0
#     b = 1
#
#     while b < len(a) and a1 < len(a):
#
#         fir_pos = str(a[a1])
#         sec_pos = str(a[b])
#         if len(fir_pos) == len(sec_pos):
#             if fir_pos[:1] < sec_pos[:1]:
#                 a1 += 1
#             elif fir_pos[:1] == sec_pos[:1]:
#                 if fir_pos < sec_pos and sec_pos[-1] != 0:
#                     a1 += 1
#                 else:
#                     b += 1
#             else:
#                 b += 1
#         elif len(fir_pos) > len(sec_pos):   # 67 > 6
#             if fir_pos[:1] < sec_pos[:1]:   # 6 < 9
#                 a1 += 1
#             elif fir_pos[:1] == sec_pos[:1]:  #
#                 if fir_pos > sec_pos and a[a1]%10 != 0:
#                     a1 += 1
#                 else:
#                     b += 1
#             else:
#                 b += 1
#
#         else:
#             if fir_pos[:1] < sec_pos[:1]:
#                 a1 += 1
#             elif fir_pos[:1] == sec_pos[:1]:
#                 if fir_pos < sec_pos and a[b]%10 != 0:
#                     a1 += 1
#                 else:
#                     b += 1
#             else:
#                 b += 1
#     res += str(a.pop(a1))
#     # print(res)
#     # break
# print(res)
#
#
#
#
# # 9954323522512319