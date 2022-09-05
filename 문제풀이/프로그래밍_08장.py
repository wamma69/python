#1
class Cat:
    def __init__(self, xname, xage):
        self.__name = xname
        self.__age = xage
        
    def __str__(self):
        msg = self.__name + " " + str(self.__age)
        return msg
    
    def setName(self, xname):
        self.__name = xname
        
    def setAge(self, xage):
        self.__age = xage
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    
missy = Cat("missy", 3)
lucky = Cat("lucky", 5)
print(missy)
print(lucky)

missy.setAge(7)
print(missy.getAge())

lucky.setName("lulu")
print(lucky.getName())
    
        
#2
class Rocket:
    def __init__(self, rx=0, ry=0):
        self.x = rx
        self.y = ry
        
    def __str__(self):
        msg = "로켓의 높이:" + str(myRocket.y)
        return msg
        
    def moveUp(self):
        self.y += 1
        
myRocket = Rocket()
print(myRocket)

myRocket.moveUp()
print(myRocket)


#4
class Rectangle:
    def __init__(self,rx,ry,rw,rh):
        self.__x = rx
        self.__y = ry
        self.__width = rw
        self.__height = rh
        
    def __str__():
        pass
    
    def setX(self, rx):
        self.__x = rx

    def setY(self, ry):
        self.__y = ry        
        
    def setWidth(self, rw):
        self.__width = rw

    def setHeight(self, rh):
        self.__height = rh

    def getX(self):
        return self.__x        
        
    def getY(self):
        return self.__y  

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height   
    
    def getArea(self):
        return self._width * self.__height
    
    def overlap(self, r):
        if (self.__x + self.__width >= r.__x ) and (self.__y + self.__height >= r.__y) :
            return True 
        else :
            return False
        
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)

if r1.overlap(r2) == True :
    print("r1과 r2는 서로 겹침니다.")
else :
    print("r1과 r2는 서로 겹치지 않습니다.")
    
#5
class Triangle:
    numberOfsides = 3
    
    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3
        
    def __str__(self):
        pass
    
    def setAngle(self, a1, a2, a3):
        pass
    
    def getAngle(self):
        pass
    
    def checkAngle(self):
        if self.angle1 + self.angle2 + self.angle3 == 180 :
            return True
        else :
            return False
            
triangle = Triangle(90, 30, 60)
print(triangle.checkAngle())
            
#7
class PhoneBook :
    contacts = dict()
    MyList = []
    
    def __init__(self):
        pass
        
    def __str__(self):
        s = ""
        for i in PhoneBook.MyList:
            s = s + i["name"] + "\n"
            s = s + "mobile phone: " + str(i["mobile"]) + "\n"
            s = s + "office phone: " + str(i["office"]) + "\n"            
            s = s + "email address: " + str(i["email"]) + "\n"
            s = s + "\n"
        return s
        
        
    def add(self, name, mobile=None, office=None, email=None):
        PhoneBook.contacts = dict()
        PhoneBook.contacts["name"] = name
        PhoneBook.contacts["mobile"] = mobile 
        PhoneBook.contacts["office"] = office
        PhoneBook.contacts["email"] = email 
        PhoneBook.MyList.append(PhoneBook.contacts)

        
obj = PhoneBook()
obj.add("kim", office="1234567", email="peterchokr@gmail.com")
obj.add("park", office="2345678", email="park@company.com")
print(obj)    
        
        
    

