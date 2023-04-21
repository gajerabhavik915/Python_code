print('this is for exceptional handling')
#
# def division(a, b):
#     print('this function is for division')
#
#     try:
#         print(a/b)
#     # except ZeroDivisionError :
#     #     print('please provide divisible value')
#     except TypeError:
#         raise ValueError('please provide proper int value')
#     else:
#         if a < 0:
#             print('please provide value greater than zero.')
#     finally:
#         return 'This code executed'
#
# print(division(6,'ddd'))


def division(a, b):
    print('this function is for division')

    try:
        print(a/b)
    except ZeroDivisionError :
        print('please provide divisible value')
    # except ZeroDivisionError:
    #     print('please provide divisible value')
    except TypeError:
        if isinstance(b, int) or isinstance(b, float):
            raise ValueError('please provide proper int value')
        else:
            raise
    else:
        if a < 0:
            print('please provide value greater than zero.')
    finally:
        return 'This code executed'

print(division(6,'ddd'))