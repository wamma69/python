import turtle
t = turtle.Turtle()
t.shape("turtle")
color =input("색상(blue, red, yellow만 가능):")
t.color(color)

while True:
    print("거리와 각도를 입력하시오.")
    degree = int(input("거북이 회전 각도(left):"))
    distance = int(input("거북이 전진 거리:"))
    t.left(degree)
    t.fd(distance)
    print("제어에 성공하였습니다. ")
    
turtle.done()