print('This programme is for understanding of global and local variable')

# a = 10
# def local():
#     a = 15
#     print(a)
#
# local()
# print(a)

##output###
# 15
# 10

#--------------------------------------------------------

# # a = 20
# def local():
#     print(a)
#
# local()
# print(a)

###output###
# 20
# 20

#---------------------------------------------------------

def local():
    a = 30
    print(a)

local()
print(a)

###output###
# 30
# NameError: name 'a' is not defined

