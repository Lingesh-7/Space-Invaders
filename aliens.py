from turtle import Turtle


LEVEL=[200,230,260,290]
class Alien:
    def __init__(self,shape_):
        self.aliens_=[]
        self.xm=10
        self.ym=10
        self.msp=0.1
        j=0
        while j<=3:
            for i in range(-150,150,40):
                alien=Turtle(shape=shape_)
                alien.color('green')
                alien.penup()
                alien.goto(i,LEVEL[j])
                self.aliens_.append(alien)
            j+=1
        # self.move_right() 
        # self.move()
        
    def move(self):
        self.move_right()
        for i in self.aliens_:
            if i.xcor()>320:
                self.move_left()
            

    def move_right(self):
        for i in self.aliens_:
            i.goto(x=i.xcor()+self.xm,y=i.ycor())

    def move_left(self):
        for i in self.aliens_:
            i.goto(x=self.xm-i.xcor(),y=i.ycor())
            # i.goto(x=self.xm+i.xcor(),y=i.ycor())

   