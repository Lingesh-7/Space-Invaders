from turtle import Turtle


class BomB(Turtle):
    def __init__(self,cord,colors):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.color(colors)
        self.penup()
        self.goto(cord)
        self.xm=10
        self.ym=10
        self.msp=0.1

    def move_alien(self):
        self.bomb_in_diff=[]
        
        self.goto(x=self.xcor(),y=self.ycor()-self.ym)
        
    def move_space(self):
        self.goto(x=self.xcor(),y=self.ycor()+self.ym)

