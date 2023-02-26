print('this is for star number')
for a in range(2,6):
    for i in range(1,a):
        print(i, end='')
    print(end='\n')

###OutPut###
# this is for star number
# 1
# 12
# 123
# 1234
#---------------------------------------------------------------

print('this is for star number')
for a in range(1,6):
    print((str(a))*a)
    # print(('*')*a)

###output###
# 1
# 22
# 333
# 4444
# 55555

# ------------------------------------------------------------
print('this is for star design')

for a in range(1,10):
    if a >= 3 and a < 9:
        print('*', end = '')
        print(' '*(a-2), end = '')
        print('*')

    else:
        print('*'*(a))

###output###
# this is for star design
# *
# **
# * *
# *  *
# *   *
# *    *
# *     *
# *      *
# *********
##------------------------------------------------------------------------------------
for a in range(0, 5):
    for b in range(0, 5):
        if a == 0 or b == (4) or a==b:
            print('*', end = '')

        else:
            print(end = ' ')

    print()

###output###
# *****
#  *  *
#   * *
#    **
#     *


## Below code is for universal above star design
a = '*'
b = int(input('what are the rows you want?'))
for i in range(1,b):
    if i>1:
        print((' ')*(i-1), end = '')
        print(('*'), end = '')
        if i < b-2:
            print((' ')*(b-2-i), end = '')
        if i < b-1:
            print('*')
    else:
        print(a*(b-1))

###output###
# what are the rows you want?7
# ******
#  *   *
#   *  *
#    * *
#     **
#      *


# ------------------------------------------------------
# for a in range(6, 0, -1):
#     if a < 6 and a > 2:
#         print("*", end = '')
#         print((' ')*(a-2), end = '')
#         print('*')
#     else:
#         print('*'*(a))
#
# for a in range(6, 0, -1):
#     if a < 6 and a > 2:
#         print(' '*(6-a), end = '')
#         print('*', end = '')
#         print(' '*(a-2), end = '')
#         print('*')
#     else:
#         print(' ' * (6 - a), end='')
#         print('*'*(a))

# ---------------------------------------------------------------
#
# print('This is for number')
# num = 1
# for a in range(1,6):
#     for b in range(1, a+1):
#        print(num, end = '')
#        num = num + 1
#     print(end = '\n')
#
# --------------------------------------------------------------
# #
# a = 'python'
# for b in range(len(a)+1):
#     print(a[:b])

# -------------------------------------------------------------

# print('This is for number')
#
# for a in range(6,0,-1):
#     for b in range(1,a+1):
#         print(b, end = '')
#     print()
#
# print('This is for number')
# space = ' '
# for a in range(6, 0, -1):
#     print(space * (6-a), end='')
#     for b in range(1, a+1):
#
#         print(b, end = '')
#     print()
#
# # --------------------------------------
# print('this is for same number')
# space = ' '
# for a in range(6, 0, -1):
#     print(space*(6-a), end = '')
#     print(str(a)*a, end = '\n')
# print(end = '')

# --------------------------------------

# print('this is for prime number')
#
# for a in range(2,100):
#     for b in range(2, a):
#         if a%b == 0:
#             # print('This is not a prime number')
#             break
#     else:
#         print(a)

# ----------------------------------------

# print('this is to check that the number is prime or not')
#
# a1 = int(input('what is your expected number'))
# for a in range (2, a1):
#     if a1%a == 0:
#         print('This is not prime')
#         break
# else:
#     print(f'The given number {a1} is prime')

# -----------------------------------------------------
# print('this is for star triangle shape')
# a1 = int(input('enter your expected rows'))
# for a in range(1,a1+1):
#     for b in range(1,a1*2):
#         if a == a1 or a+b == a1+1 or b-a == a1-1:
#             print('*', end = '')
#         else:
#             print(end = ' ')
#     print()

# print('This is another triangle shape')
# n = int(input('Enter your expected number'))
# for rows in range(1, n+1):
#     for columns in range(1, 2*n):
#         if rows != n and (rows + columns == n+1 or columns-rows == n-1):
#             print('*', end = '')
#         elif rows == n:
#             print('* '*(n))
#             break
#         else:
#             print(end = ' ')
#     print()

# ---------------------------------------------------------------

# for rows in range(1,6):
#     for columns in range(1,6):
#         if rows == columns or rows == 1 or columns == 5:
#             print('*', end = '')
#         else:
#             print(end = ' ')
#     print()
# #
# space = ' '
# for a in range(5, 0, -1):
#     if 5 > a > 2:
#         print(' '*(5-a), end = '')
#         print('*', end = '')
#         print(' '*(a-2), end = '')
#         print('*')
#     else:
#         print(' '*(5-a), end='')
#         print('*'*(a))
# -------------------------------------------------------------------
#
# for a in range(1, 7):
#     for b in range(1, 7):
#         if a == b or a>b:
#             print('*', end = '')
#         else:
#             print(end = '')
#     print()
# ------------------
# for a in range(1,7):
#     print('*'*(a))
#
# n = int(input("How many rows do you want to print?"))
# for a in range(1, n+1):
#     print(' '*(n-a), end = '')
#     print('* '*(a), end = '\n')

# -----------------------------------------------------------------

# print('This is for rectangle shape')
#
# for rows in range(1,6):
#     for columns in range(1,6):
#         if rows+columns == 4 or rows+columns == 8 or rows-columns == 2 or rows-columns == -2:
#             print('*', end = '')
#         else:
#             print(end = ' ')
#     print()
#
# # universal
# n = int(input('Enter your expected rows'))
# a = ((n+1)/2)
# for rows in range(1,n+1):
#     for columns in range(1,n+1):
#         if rows+columns == (((n+1)//2)+1) or rows+columns == a+n or rows-columns == (((n+1)//2)-1) or rows-columns == -(((n+1)//2)-1):
#             print('*', end = '')
#         else:
#             print(end = ' ')
#     print()

# ---------------------------------------------------------
#
# print('This is for number in triangle shape')
#
# space = ' '
# for a in range(1,5):
#     print(space*(4-a), end = '')
#     for b in range(a, 0, -1):
#         print(b, end = '')
#     for c in range(2, a+1):
#         print(c, end = '')
#     print()
# ------------------------------------------------------------

# print('This is for increment number')
# num = 1
# for a in range(1, 6):
#     # print(' '*(5-a), end = '')
#     for b in range(1, a+1):
#         print(num, end = ' ')
#         num = num+1
#     print()

# -----------------------------------------------------------

# print('This is for reserve number in triangle shape')
#
# num = 15
# for a in range(1,6):
#     for b in range(1, a+1):
#         if num <= 9:
#             print(num, end = '  ')
#             num = num -1
#         else:
#             print(num, end = ' ')
#             num = num - 1
#     print()

# ---------------------------------------------------------
#
# print('This is for X-shape')

# for rows in range(5):
#     for columns in range(5):
#         if rows == columns:
#             print(columns + 1, end = ' ')
#         elif columns + rows == 4:
#             print(rows+1, end = ' ')
#         else:
#             print(' ', end = ' ')
#     print(end = '\n')
#
# ---------------------------------------------------
#
# print('This is for triple digit')
#
# for a in range(5):
#     for b in range(1, a+2):
#         print(str(b)*3 , end = ' ')
#     print()

# i = 0
# while i < 5:
#     for a in range(1, i +2):
#         print(str(a)*3, end = ' ')
#     print()
#     i = i+1
#
# -----------------------------------------------------

# print('This is for triple digit')
# space = (' ')
# for a in range(1,6):
#     print(space*(5-a), end='')
#     for b in range(a, 0, -1):
#         print((b) , end = '')
#     print()

# ------------------------------------------------------
#
# for rows in range(0,5):
#     for columns in range(5):
#         if rows + columns <= 3:
#             print('*', end = '')
#     print()
# -----------------------------------------------------------------

# for rows in range(0,4):
#     print(' ' * (3 - rows), end='')
#     for columns in range(rows+1,0,-1):
#         print(columns, end = '')
#     if rows >= 1:
#         for more in range(2,rows+2):
#             print(more, end = '')
#     print()

# ----------------------------------------------------------------

# for a in range(0,4):
#     for b in range(0,7):
#        if a == 0 or a+b == 6 or a==b:
#            print('*', end = '')
#        else:
#            print(end = ' ')
#     print()
#

# --------------------------------------------------------------

# for rows in range(1,5):
#     for columns in range(1,5):
#         if rows + columns >= 5:
#             print('*', end = '')
#         else:
#             print(end = ' ')
#     for more in range(rows, rows*2):
#         print(more, end = '')
#     print()

