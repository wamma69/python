#1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "점의 위치 : " + "(" + str(self.x) + "," + str(self.y) + ")"
    
class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    def __str__(self):   #mothod overriding
        return "점의 위치 : " + "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

x = Point(3, 4)  
print(x)
 
y = Point3D(6,7,8)
print(y)

#2
class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
        
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class Contact(Address, Person):  #다중상속
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)
        
    def __str__(self):
        return "이름 : " + self.name + ", " + "주소 : " + self.city + self.street + ", " + "메일 : " + self.email
    
x = Contact("현충로 170", "대구시", "조정현", "peterchokr@gmail.com" )
print(x)

#3
import math

class Function:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def value(self):
        return 0
    
class Quadratic(Function):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
        
    def value(self):    #mothod overriding
        return self.get_root()
    
    def get_root(self):
        x1 = (-self.b + math.sqrt(self.b ** 2 - (4 * self.a * self.c))) / (2 * self.a)
        x2 = (-self.b - math.sqrt(self.b ** 2 - (4 * self.a * self.c))) / (2 * self.a)
        return x1, x2
        
f = Quadratic(1, 2, -3)
print(f.value())
        
#4
import random

class Dice:
    def __init__(self):
        pass
    
    def roll(self):
        return random.randint(1, 6)
    
class FraudDice(Dice):
    def __init__(self):
        super().__init__()
        
    def roll(self):  #mothod overriding
        x = 1
        while x <= 3:
            x = super().roll()
        return x
    
game = FraudDice()
print(game.roll())