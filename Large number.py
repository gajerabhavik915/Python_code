# a = [3,30,34,5,9]
#
#
# # a = [90,9]
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
#             elif fir_pos[:1] == sec_pos[:1]:  # 99 9
#                 if fir_pos > sec_pos and a[b]%10 != 0: #90 9
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
# #
# #
# #
# #
# # # 9954323522512319



nums = [3322211, 33222]  #111311 1113  #1113 111113
for i in range(len(nums)):
    first = 0
    sec = 1
    while first < len(nums) and sec < len(nums):
        str_fst = str(nums[first])
        str_sec = str(nums[sec])

        if len(str_fst) < len(str_sec):   # 3 30,
            if str_fst[:1] < str_sec[:1]:  # 2 33
                first += 1
            elif str_fst[:1] == str_sec[:1]: # 3 30
                if int(str_sec)%10 == 0:
                    sec += 1
                else:
                    first += 1
            else:
                sec += 1

        if len(str_fst) == len(str_sec):
            if str_fst[:1] > str_sec[:1]:  # 99, 88
                sec += 1
            elif str_fst[:1] == str_sec[:1]:
                if str_fst < str_sec:  # 22, 20   99909988 99889990
                    first += 1
                else:
                    sec += 1
            else:  # 88, 90    #9088 #8890  #88 90
                first += 1

        if len(str_fst) > len(str_sec):  # 22 #9
            if str_fst[:1] > str_sec[:1]:  # 99, 3
                sec += 1
            elif str_fst[:1] == str_sec[:1]:  # 22111122 221111 22111122-221111 221111-22111122
                if (len(str_fst) and len(str_sec)) > 1 and nums[first]%10 != 0 and nums[sec]%10 != 0:
                    fir_place, sec_place = 1,1
                    while fir_place < len(str_fst) and sec_place < len(str_sec):
                        if str_fst[fir_place] == str_sec[sec_place]:
                            fir_place += 1
                            sec_place += 1
                        elif str_fst[fir_place] < str_sec[sec_place]:
                            first += 1
                            break
                        else:
                            sec += 1
                            break
                            # 33222115 33222    33222115-33222    33222-33222115
                    else:
                        if fir_place < len(str_fst):
                            fir_place = fir_place
                            while fir_place < len(str_fst):
                                if str_fst[fir_place] > str_sec[sec_place - 1]:
                                    sec += 1
                                    break
                                # elif str_fst[fir_place] < str_sec[sec_place]:
                                fir_place += 1

                            else:
                                first += 1







                elif nums[first] % 10 == 0:  # 90 9
                    first += 1
                else:
                    sec += 1
            else:
                first += 1



    val = nums.pop(first)
    print(val, nums)













