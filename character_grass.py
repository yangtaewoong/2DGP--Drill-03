from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('Circle')
    clear_canvas_now()
    character.draw_now(400,300)
    delay(0.1)


    
    pass

def run_rectangle():
    print('Rectangle')
    pass


while True:
    run_rectangle()
    run_circle()


close_canvas()
