print('Let\'s understand what is Lambda function')


# what is need of lambda function

# without lambda func. we have to write more lines of code.
def add(a,b):
    return a+b
obj = add(2,3)
print(obj)


# whereas, with lambda func. within one list we can get result.
obj = lambda a,b : a+b
print(obj(2,3))

# ----------------------------------------------------------------------

# we can explicitly define the value inside lambda func. as same as actual func.
obj = lambda a,b = 2 : a+b
print(obj(5))

# we can change order, while giving value.
obj = lambda x,y,z : x+y*z
print(obj(z=5, y=2, x=3))

# how to pass arg in lambda function.
obj = lambda *args : sum(args)
print(obj(4,10,20,25))

# how can we write fun inside lambda function
obj = lambda a, fun : a+fun(a)
obj(3, lambda a: a*a)

# how can we add conditional arg.
obj = lambda a: True if a%2==0 else False
print(obj(5782526))
# Now, Let's understand how to apply filter, map and reduce in lambda function

# Let's first understand, what is need of filter and how to apply it.

# without filter and lambda
list1 = [1,2,3,4,5,6,7]

def filter(list2):
    l = []
    for i in list2:
        if i%2 == 0:
            l.append(i)
    return l

print(filter(list1)) # [2,4,6]

# with filter and lambda
x = [1, 2, 3, 4, 5, 6, 7]

# obj = list(filter(lambda x : x%2 ==0, x))
# print(obj)

# how to use map in lambda
obj = list(map(lambda x : x*2, x))
print(obj)

# how to use reduce in lambda
from functools import reduce

obj = (reduce(lambda a,b: a+b, x))
print(obj)


