# 메소드 오버라이딩(method overriding)

import math

class Shape:
     def __init__(self):
        pass

     def draw(self):
        print("뭔가를 그립니다.")

     def get_area(self):
        print("뭔가의 면적을 구합니다.")

class Circle(Shape):
     def __init__(self, radius=0):
        super().__init__()
        self.radius = radius
 
     def draw(self):        #오버라이딩(overriding)
        print("원을 그립니다.")

     def get_area(self):    #오버라이딩(overriding)
        return math.pi * self.radius ** 2 

c = Circle(10)
c.draw()
print("원의 면적:", c.get_area())