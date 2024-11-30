from turtle import Screen,TK
from aliens import Alien
from barrier import RectangleBarrier
from spaceship  import SpaceShip
from bomb import BomB
from random import choice
import time
import keyboard


my_screen=Screen()
# img1='👾'
# img2='🛸'
# my_screen.addshape(img1)
# my_screen.addshape(img2)
my_screen.tracer(0)
my_screen.title('SPACE INVADERS 👾👽')

my_screen.bgcolor('black')
my_screen.setup(700,650)

alien_=Alien(shape_='square')

barrier=RectangleBarrier()

space_ship_=SpaceShip((0,-280),shape_='square')

bomb_x=[210,240,300,270,-290,-200,-150,-95,-70]             
bomb_of_alines=BomB((choice(bomb_x),210),colors='red')

bomb_of_spaceship=BomB((0,-280),colors='white')



my_screen.listen()
my_screen.onkey(fun=space_ship_.move_right,key='Right')
my_screen.onkey(fun=space_ship_.move_left,key='Left')

game_life=0
while True:
    if game_life==3:
        TK.messagebox.showinfo(title="Game Ended!", message="Game Over!")
        break
    time.sleep(alien_.msp)
    my_screen.update()

    bomb_of_alines.move_alien()
 
    if keyboard.is_pressed('space')==1:
        bomb_of_spaceship.move_space()


    alien_.move()

    if bomb_of_alines.ycor()<-280:
        bomb_of_alines.ht()
        bomb_of_alines=BomB((choice(bomb_x),210),colors='red')
        bomb_of_alines.move_alien()

    if bomb_of_spaceship.ycor()>280:
        bomb_of_spaceship.ht()
        bomb_of_spaceship=BomB((0,-280),colors='white')
        bomb_of_spaceship.move_space()


    #bomb collision with aliens
    for i in alien_.aliens_:
        if bomb_of_spaceship.distance(i)<20:
            i.ht()

    #bomb collision with barriers
    for i in barrier.barrier_:
        # print(bomb_of_alines.distance(i))
        if bomb_of_alines.distance(i)<50 or bomb_of_spaceship.distance(i)<50:
            i.ht()
    
    #SpaceShip COllision
    if bomb_of_alines.distance(space_ship_)<50:
        game_life+=1
        space_ship_.ht()
        space_ship_=SpaceShip((0,-280),shape_='square')
        my_screen.listen()
        my_screen.onkey(fun=space_ship_.move_right,key='Right')
        my_screen.onkey(fun=space_ship_.move_left,key='Left')


    if bomb_of_spaceship.distance(bomb_of_alines)<20:
        bomb_of_spaceship.ht()
        bomb_of_spaceship=BomB((0,-280),colors='white')
        bomb_of_spaceship.move_space()
    # print(bomb_of_alines.distance(bomb_of_spaceship))
    if bomb_of_alines.distance(bomb_of_spaceship)<30: 
        bomb_of_alines.ht()
        bomb_of_alines=BomB((choice(bomb_x),210),colors='red')
        bomb_of_alines.move_alien()  




# my_screen.mainloop()
my_screen.exitonclick()