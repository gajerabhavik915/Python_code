# class Class1:
#     no_of_leave = 8
#     pass
#
# Bhavik = Class1() #it's call instance
# Dhaval = Class1()
# Jaydip = Class1()
#
# Bhavik.name = 'Bhavik'
# Bhavik.age = 22
# Bhavik.gender = 'male'
# Bhavik.location = 'Canada'
#
# Dhaval.name = 'Dhaval'
# Dhaval.age  = 25
# Dhaval.gender = 'male'
# Dhaval.location = 'USA'
#
# print(Bhavik.age)
# print(Dhaval.location)
# print(Bhavik.no_of_leave)
# Class1.no_of_leave = 9
# print(Bhavik.__dict__)
# print(Bhavik.no_of_leave)
# #we cannot chnage the NO_OF_LEAVE through object's name like bhavik and dhaval
# #----------------------------------------------------------------------------
#
# # self
# #
# class Class1:
#     no_of_leave = 8
#
#     def fun1(self):
#         return f'this is {self.name} and his age is {self.age} and his location is {self.location}'   #self string
#
#
#
# Bhavik = Class1()
# Dhaval = Class1()
# Jaydip = Class1()
#
# Bhavik.name = 'Bhavik'
# Bhavik.age = 22
# Bhavik.gender = 'male'
# Bhavik.location = 'Canada'
#
# Dhaval.name = 'Dhaval'
# Dhaval.age  = 25
# Dhaval.gender = 'male'
# Dhaval.location = 'USA'
#
# print(Bhavik.age)
# print(Dhaval.location)
# print(Bhavik.no_of_leave)
# Class1.no_of_leave = 9
# print(Bhavik.__dict__)
# print(Bhavik.no_of_leave)
#
# print(Bhavik.fun1())
# print(Dhaval.fun1())
# #---------------------------------------------------------
#
# #__init___
# # #
# class Class1:
#     # no_of_leave = 8
#
#     def __init__(self, his_name, His_age, His_gender, His_location): #--init--constructor
#         self.name = his_name
#         self.age = His_age
#         self.gender = His_gender
#         self.location = His_location
#
#     def fun1(self):
#         return f'this is {self.name} and his age is {self.age} and his location is {self.location}'
#
#
# Bhavik = Class1('Bhavik', 22, 'male', 'canada')
# #Bhavik = Class1()
# Dhaval = Class1('Dhaval', 25, 'male', 'USA')
# # Jaydip = Class1()

# Bhavik.name = 'Bhavik'
# Bhavik.age = 22
# Bhavik.gender = 'male'
# Bhavik.location = 'Canada'
#
# Dhaval.name = 'Dhaval'
# Dhaval.age = 25
# Dhaval.gender = 'male'
# Dhaval.location = 'USA'
#
# print(Bhavik.age)
# print(Dhaval.location)
# print(Bhavik.no_of_leave)
# Class1.no_of_leave = 9
# print(Bhavik.__dict__)
# print(Bhavik.no_of_leave)
#
# print(Bhavik.fun1())
# print(Dhaval.fun1())
#
# #---------------------------------------------
# #
# class class1:
#     no_of_leave = 8
#
#     def __init__(self, his_name, his_location):
#         self.name = his_name
#         self.location = his_location
#
#     def fun1(self):
#         return f'this is {self.name}, and his location is {self.location}'
#
#     @classmethod
#     def change_leave(cls, new_no_leave):
#         class1.no_of_leave = new_no_leave
#
#     @classmethod  #if we want any changes, we can do through classmethod
#     def from_str(cls, string):
#         bhav = string.split('-')
#         print(bhav)
#         return cls(bhav[0], bhav[1])
#
#     @staticmethod    #this is just for adding string
#     def thisgood(string):
#         print('this is a good', string)
#         return ''
#
#
# bhavik = class1('Bhavik', 'Pablo')
# print(bhavik.fun1())
#
# bhavik.change_leave(10)
# print(bhavik.no_of_leave)
#
# pritesh = class1.from_str('pritesh-India')
# print(pritesh.location)
#
# class1.thisgood('Bhavik')
#
# #--------------------------------------------------------
# bhavik = class1()
# dhaval = class1()
# harsh = class1()
# om = class1()
#
# bhavik.name = 'Bhavik'
# bhavik.location = 'canada'
#
# dhaval.name ='dhaval'
# dhaval.location = 'USA'
#
# harsh.name = 'harsh'
# harsh.location = 'Dubai'
#
# om.name = 'Om'
# om.location = 'Uganda'
#
# harsh.nickname = 'Zadiyo'
# dhaval.nickname = 'bhurivalo'
#
# print(bhavik.__dict__)
# print(dhaval.fun1())
# #--------------------------------------------------
# #abstarction
#

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
#
#
# # code to calculate the total area of a collection of shapes
# shapes = [Rectangle(3, 4), Rectangle(5, 6), Circle(2), Circle(4)]
# # circles = [Circle(2), Circle(4)]
# total_area = 0
#
# # calculate area of all rectangles
# for shape in shapes:
#     total_area += shape.area()
#
# # # calculate area of all circles
# # for circle in circles:
# #     total_area += circle.area()
#
# print(total_area)

from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# code to calculate the total area of a collection of shapes
shapes = [Rectangle(3, 4), Rectangle(5, 6), Circle(2), Circle(4)]
total_area = 0

# calculate area of all shapes
for shape in shapes:
    total_area += shape.area()

print(total_area)
