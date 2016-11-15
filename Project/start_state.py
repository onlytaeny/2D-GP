import game_framework
import title_state
from pico2d import *
import os


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    os.chdir('resource')
    image = load_image('bgi\\bg_title2.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if(logo_time > 2.00):
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass