# 정보 은닉

# 1 외부에서 인스턴스 변수의 값을 변경하고 있다 -> 좋은 방법이 아니다.
class Student:
	def __init__(self, name=None, age=0):
		self.name = name	
		self.age = age		
  
obj=Student("Hong", 20)
obj.age = 21
print(obj.age)		


# 2  클래스 내부에서만 접근될 수 있다. private
class Student:
	def __init__(self, name=None, age=0):
		self.__name = name	# __가 변수 앞에 붙으면 외부에서 변경 금지
		self.__age = age		# __가 변수 앞에 붙으면 외부에서 변경 금지

obj=Student()
print(obj.__age)			# 오류 발생!

