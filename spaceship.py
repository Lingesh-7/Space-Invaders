from turtle import Turtle


class SpaceShip(Turtle):
    def __init__(self,cord,shape_):
        super().__init__()
        new_img="🛸"
        # self.space_ship=Turtle('square')
        # self.register_shape(new_img)
        self.shape(shape_)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color('green')
        self.penup()
        self.goto(cord)

    def move_right(self):
        self.x_=self.xcor()+20
        self.goto(self.x_,self.ycor())
    
    def move_left(self):
        self.x_=self.xcor()-20
        self.goto(self.x_,self.ycor())
