print('this is for decorator')
#
# def fun1(dec1):
#     def inner():
#         print('this will be printed first')
#         dec1()
#         print('this will be printed second')
#     return inner
#
# def dec1():
#     print('This will be printed in middle')
#
# dec1 = fun1(dec1)
# dec1()

#------------------------------------------------------------
#('suppose we have already created fun for division')



# dev(4,2)

#suppose first value is smaller than second value.

def small(dev):
    def inner(a,b):
        if a<b:
            a,b = b,a
            dev(a,b)
        else:
            dev(a,b)
    return inner
@small
def dev(a,b):
    print(a/b)

# dev = small(dev)
dev(2,8)
