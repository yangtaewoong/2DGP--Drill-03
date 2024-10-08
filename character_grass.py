from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x,y):
    clear_canvas_now()
    character.draw_now(x,y)
    delay(0.1)  



    
def run_circle():
    print('Circle')

    r, cx, cy = 300 , 800//2 , 600//2

    for degree in range(0,360, 3):

        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_character(x, y)
             
    pass

def run_top():
    print('Top')
    for x in range(0,800, 10):
        draw_character(x, 550)
            
    pass

def run_right():
    print('Right')
    for y in range(550, 0, -10):
        draw_character(790, y)
    pass

def run_botoom():
    print('Bottom')
    for x in range(790, 0, -10):
        draw_character(x, 90)
    pass

def run_left():
    print('Left')
    for y in range(90, 550, 10):
         draw_character(0, y)
    pass

def run_rectangle():
    print('Rectangle')
    run_top()
    run_right()
    run_botoom()
    run_left()

    pass
def run_tribottom():
    print('tribottom')
    for x in range(200, 600, 10):
        draw_character(x, 90)
    pass

def run_leftdiagonal():
    print('leftdiagonal')
    y = 490
    for x in range(400, 200, -10):
        y = y - 20
        draw_character(x,y)
    pass

def run_rightdiagonal():
    print('rightdiagonal')
    y = 90
    for x in range(600, 400, -10):
        y = y + 20
        draw_character( x,y)
    pass

def run_triangle():
    print('Triangle')
    run_tribottom()
    run_rightdiagonal()
    run_leftdiagonal()
    
    pass


while True:
    run_circle()
    run_rectangle()
    run_triangle()   
    break

close_canvas()
