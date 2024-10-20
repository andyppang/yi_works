# 抬笔：penup()
# 落笔：pendown()
# 移动位置：goto()
# 计算旋转度数
# 绘制一个太极八卦图
# 画一个奥运五环

# 如何计算goto()位置

# 确定抬笔和落笔的时间
# 绘制古铜钱，通过圆形与正方形组合绘制
import turtle
x = 270
r = 30
turtle.color("gold")
turtle.speed(10)
turtle.circle(200)
turtle.circle(100,180)              
turtle.circle(-100,180)          
turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.circle(30)
turtle.penup()
turtle.goto(0,270)
turtle.pendown()
turtle.circle(30)
for i in range(28):
    x=x+1
    r=r-1
    turtle.penup()
    turtle.goto(0,x)
    turtle.pendown()
    turtle.circle(r)
    
