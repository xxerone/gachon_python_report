import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
# 거북이를 3배 확대한다. 
t.shapesize(3, 3)
while True: 
 command = input("명령을 입력하시오: ")
 if command == "l": # 사용자가 “l“을 입력하였으면
t.left(90)
 t.forward(100)
 if command == "r": # 사용자가 “r“을 입력하였으면
t.right(90)
 t.forward(100)
 if command == "q": # 사용자가 “q“을 입력하였으면
break # 무한 루프를 빠져나간다. 
turtle.mainloop()
turtle.bye()
