import time
import turtle

def startWords():
    turtle.speed(12)
    turtle.penup()
    turtle.goto(-430,320)
    turtle.pendown()

    time.sleep(2)
    turtle.speed(3)
    turtle.pencolor('blue')
    turtle.write('给可爱的：^_^',font=('Arial',9,'normal'))
    
    turtle.speed(12)
    turtle.penup()
    turtle.goto(-430,300)
    turtle.pendown()

    time.sleep(1)
    turtle.speed(3)
    turtle.pencolor('purple')
    turtle.write('@美丽的姑娘',font=('Arial',9,'normal'))

    turtle.speed(12)
    turtle.penup()
    turtle.goto(-430,280)
    turtle.pendown()

    time.sleep(1)
    turtle.speed(3)
    turtle.pencolor('red')
    turtle.write('@My Girl',font=('Arial',9,'normal'))

def roseDraw():
    #画前准备
    turtle.speed(12)
    turtle.penup()
    turtle.goto(0,-450)
    turtle.pendown()
    
    time.sleep(1)
    turtle.speed(6)
    turtle.seth(140)
    turtle.pensize(4)
    turtle.pencolor("black")
    
    #画第一片叶子
    turtle.circle(-300,60)
    turtle.fd(80)
    turtle.seth(10)
    turtle.fd(50)
    
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(40)
    turtle.circle(120,80)
    turtle.left(100)
    turtle.circle(120,80)
    turtle.end_fill()
    
    turtle.seth(10)
    turtle.fd(90)
    
    #画第二片叶子
    turtle.penup()
    turtle.fd(-140)
    turtle.pendown()
    
    turtle.seth(80)
    turtle.fd(50)
    turtle.seth(160)
    turtle.fd(50)
    
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(40)
    turtle.circle(120,80)
    turtle.left(100)
    turtle.circle(120,80)
    turtle.end_fill()
    
    turtle.seth(160)
    turtle.fd(90)
    
    #画右侧花瓣
    turtle.penup()
    turtle.fd(-140)
    turtle.pendown()
    
    turtle.seth(80)
    turtle.fd(80)
    turtle.seth(-20)
    
    turtle.fillcolor("crimson")
    turtle.begin_fill()
    turtle.circle(100,100)
    turtle.circle(-110,70)
    turtle.seth(179)
    turtle.circle(223,76)
    turtle.end_fill()
    
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(180)
    turtle.circle(-223,60)
    turtle.seth(70)
    turtle.circle(-213,15)
    turtle.left(70)
    turtle.circle(200,70)
    turtle.seth(-80)
    turtle.circle(-170,40)
    turtle.circle(124,94)
    turtle.end_fill()
    
    #画花蕊
    turtle.penup()
    turtle.right(180)
    turtle.circle(-124,94)
    turtle.circle(170,40)
    turtle.pendown()
    
    turtle.seth(-60)
    turtle.circle(175,70)
    turtle.seth(235)
    turtle.circle(300,12)
    turtle.right(180)
    turtle.circle(-300,12)
    turtle.seth(125)
    turtle.circle(150,60)
    turtle.seth(70)
    turtle.fd(-20)
    turtle.fd(20)
    turtle.seth(-45)
    turtle.circle(150,40)
    turtle.seth(66)
    turtle.fd(-18.5)
    turtle.fd(18.5)
    turtle.seth(140)
    turtle.circle(150,27)
    turtle.seth(60)
    turtle.fd(-8)
    
    #画左侧花瓣
    turtle.penup()
    turtle.left(20.8)
    turtle.fd(-250.5)
    turtle.pendown()
    
    turtle.fillcolor("crimson")
    turtle.begin_fill()
    turtle.seth(160)
    turtle.circle(-140,85)
    turtle.circle(100,70)
    turtle.right(165)
    turtle.circle(-200,32)
    turtle.seth(-105)
    turtle.circle(-170,14.5)
    turtle.circle(123,94)
    turtle.end_fill()

def endWords():
    turtle.speed(12)
    turtle.penup()
    turtle.goto(350,-250)
    turtle.pendown()
    
    time.sleep(2)
    turtle.seth(0)
    turtle.speed(3)
    turtle.pencolor('blue')
    turtle.write("来自：^_^",font=('Arial',9,'normal'))
    
    turtle.speed(12)
    turtle.penup()
    turtle.goto(350,-270)
    turtle.pendown()
    
    time.sleep(1)
    turtle.seth(0)
    turtle.speed(3)
    turtle.pencolor('purple')
    turtle.write("@爱你的汉子",font=('Arial',9,'normal'))
    
    turtle.speed(12)
    turtle.penup()
    turtle.goto(350,-290)
    turtle.pendown()
    
    time.sleep(1)
    turtle.seth(0)
    turtle.speed(3)
    turtle.pencolor('red')
    turtle.write("@You Boy",font=('Arial',9,'normal'))

def myGirl():
    #draw 'My'
    turtle.speed(12)
    turtle.penup()
    turtle.goto(-200,-160)
    turtle.pendown()
    
    time.sleep(2)
    turtle.seth(0)
    turtle.speed(3)
    #turtle.pensize()
    turtle.pencolor('purple')
    turtle.write("My Girl:",font=('Arial',16,'normal'))
    
    """
    #draw 'Girl'
    turtle.speed(12)
    turtle.penup()
    turtle.goto(,-160)
    turtle.pendown()
    
    time.sleep(2)
    turtle.seth(0)
    turtle.speed(3)
    #turtle.pensize()
    turtle.pencolor('purple')
    turtle.write("My",font=('Arial',20,'normal'))
    """
    
    #draw 'I'
    turtle.speed(12)
    turtle.penup()
    turtle.goto(-80,-200)
    turtle.pendown()
    
    time.sleep(2)
    turtle.seth(0)
    turtle.speed(3)
    #turtle.pensize()
    turtle.pencolor('blue')
    turtle.write("I LOVE YOU",font=('Arial',24,'normal'))
    
    """
    #draw 'Love'
    turtle.speed(12)
    turtle.penup()
    turtle.goto(-90,-160)
    turtle.pendown()
    
    time.sleep(1)
    turtle.seth(0)
    turtle.speed(3)
    #turtle.pensize()
    turtle.pencolor('purple')
    turtle.write("LOVE",font=('Arial',24,'normal'))
    
    #draw 'You'
    turtle.speed(12)
    turtle.penup()
    turtle.goto(60,-160)
    turtle.pendown()
    
    time.sleep(1)
    turtle.seth(0)
    turtle.speed(3)
    #turtle.pensize()
    turtle.pencolor('purple')
    turtle.write("You",font=('Arial',24,'normal'))
    """
    
def drawGap():
    turtle.penup()
    turtle.fd(1)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(6)
    drawGap()
    turtle.right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(4)
def dateDraw(data):
    turtle.speed(12)
    turtle.penup()
    turtle.goto(315,-310)
    turtle.pendown()
    
    time.sleep(2)
    turtle.seth(0)
    turtle.speed(20)
    turtle.pensize(2)
    turtle.pencolor('blue')
    
    for i in data:
        if i=='-':
            turtle.write('Y',font=('Arial',8,'normal'))
            turtle.pencolor('purple')
            turtle.fd(12)
        elif i=='=':
            turtle.write('M',font=('Arial',8,'normal'))
            turtle.pencolor('green')
            turtle.fd(12)
        elif i=='+':
            turtle.write('D',font=('Arial',8,'normal'))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(900, 700, 200, 20)
    
    startWords()
    roseDraw()
    myGirl()
    endWords()
    dateDraw(time.strftime('%Y-%m=%d+', time.gmtime()))
    
    turtle.hideturtle()
    turtle.done()
    
    time.sleep(9)

main()
