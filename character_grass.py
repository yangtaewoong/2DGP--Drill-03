from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90

tri_size = 200;
circle_size = 200;

stop = True
while (stop):
    while (x < 400 + tri_size):
        #Game Rendering
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
    
        #Game Logic
        x += 2
        delay(0.01)
    while (x > 400 and y < 490):
        #Game Rendering
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
    
        #Game Logic
        x -= 1
        y += 1.2
        delay(0.01)
    while (x > 400 - tri_size and y > 90):
        #Game Rendering
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
    
        #Game Logic
        x -= 1
        y -= 1.2
        delay(0.01)
    while (x < 400):
        #Game Rendering
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
    
        #Game Logic
        x += 2
        delay(0.01)
    delay(1)
    for i in range(-90,270):
        #Game Rendering
        clear_canvas()
        grass.draw(400,30)
        character.draw(x,y)
        update_canvas()
    
        #Game Logic
        x = 400 + (math.cos((i * math.pi / 180)) * circle_size)
        y = 90 + circle_size + (math.sin((i * math.pi / 180)) * circle_size)
        delay(0.01)
    delay(1)

close_canvas()
