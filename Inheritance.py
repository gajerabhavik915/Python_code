print('This is for understanding all Inheritance types')

# Let's first understand simple inheritance
class All_calculation:                  #it's called parent class
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(f'addition of two given number is {self.a + self.b}')
    def substraction(self):
        return f'substraction of two given number is {self.a-self.b}'

class Number(All_calculation):          #it's called subclass or drived class or child class

    def multi(self):
        return f'multification of two given number is {self.a * self.b}'


obj = Number(3,2)
obj.add()
obj = All_calculation(1,2)
obj.substraction()

#-----------------------------------------------------------------------------------------------------------------

#Now, let's understand Multi-level Inheritance

class car:                                 # Grand class
    def __init__(self,name,com):
        self.name = name
        self.com = com

    def color(self):
        print('This is black car')

class speed(car):                          # Parent class
    def speed(self):
        print(f'if car name is {self.name} and company is {self.com}, speed is 100 km/h')

    def doors(self):
        print('this is two seaters car, So it may have two doors.')

class shape(speed):                         # child class
    def shape(self):
        print(f'if speed is 100km/hour, car shape might be sedan')

    def Buyer(self):
        print(f'buyer must have down payment near 10 lacs.')

obj = shape('Sedan', 'Mercedese')
obj.Buyer()
obj.speed()
obj.color()

# --------------------------------------------------------------------------------------------------------------------------


# Now, let's understand Multiple Inheritance

class standard:
    def __init__(self, name, std):
        self.name = name
        self.std = std

    def fees(self):
        print(f'standard of {self.std} is $7000')

class Subject:
    def sub(self):
        print('student has to learn total main three subjects')

    def sub_name(self):
        print('"Math", "Science", "English", "Sanskrit"')

class Student(standard, Subject):
    def Uniform(self):
        print(f'students have to wear white shirt and blue trouser')

    def Leave(self):
        print(f'Student can take leave three days off for sick')

obj = Student('Bhavik', 7)
print(obj.std)
obj.fees()
obj.sub_name()
obj.Leave()

