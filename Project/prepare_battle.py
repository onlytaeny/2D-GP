import random
import json
import os

from pico2d import *

import game_framework
import battle_menu

import Function

name = "prepare_battle"

background = None

select_menu = 0

def enter():
    global background
    background = load_image('bgi\\bg_battle_prepare.png')


def exit():
    global background
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global background_right
    global bg_move
    global select_menu
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT)):
                game_framework.change_state(battle_menu)


def update():
    pass


def draw():
    clear_canvas()
    background.draw(400, 300)
    update_canvas()