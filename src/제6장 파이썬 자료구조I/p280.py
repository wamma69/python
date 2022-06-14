# 변수 - 값에 의한 전달
def func1(x):
    x = 42
    print( "x=",x," id=",id(x))

y = 10
func1(y)
print( "y=",y," id=",id(y))


# # 리스트 - 참조에 의한 전달
# def func2(list):
#     list[0] = 99
#     print(list)
    
# values = [0, 1, 1, 2, 3, 5, 8]
# func2(values)
# print(values)