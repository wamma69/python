class Address:
    def __init__(self, street, city):
        self.street =street
        self.city = city

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)
        
    def __str__(self):
        return "이름 : "+self.name+", " + "도시 : " + self.city +", " + "거리명 " + self.street + ", " + "메일주소 " + self.email
        
c1_1 = Contact("대명로", "대구", "조", "ss@gmail.com")
print(c1_1)
