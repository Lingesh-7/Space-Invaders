from turtle import Turtle

# text="= = = = = = ="
# FONT=('corier',100,'normal')
x=[i for i in range(-320,320,90)]
class RectangleBarrier:
    def __init__(self):
        self.barrier_=[]
        # for i in range(13):
        for j in x:
            text_bar=Turtle('square')
            text_bar.shapesize(stretch_wid=1,stretch_len=4)
            text_bar.color('green')
            text_bar.penup()
            text_bar.goto(j,-70)
            self.barrier_.append(text_bar)

