import random
import json

from pico2d import *

import game_framework
import battle_menu
import shop_state

import Function

name = "MainState"

background = None
background_right = False
bg_move = False
bg_posx = 700

button_battle = None
button_shop = None
button_room = None

def enter():
    global background
    global button_battle
    global button_shop
    global button_room
    background = load_image('bgi\\bg_gensou.png')
    button_battle = load_image('image\\button_map_battle.png')
    button_shop = load_image('image\\button_map_shop.png')
    button_room = load_image('image\\button_map_room.png')


def exit():
    global background
    global button_battle
    global button_shop
    global button_room
    del(background)
    del(button_battle)
    del(button_shop)
    del(button_room)


def pause():
    pass


def resume():
    pass


def handle_events():
    global background_right
    global bg_move
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if ((event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)) and (not bg_move):
                background_right = not background_right
                bg_move = True
            elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                if Function.PointInRect(event.x, event.y, 18, 122, 565, 600):
                    game_framework.push_state(battle_menu)
                if Function.PointInRect(event.x, event.y, 128, 232, 565, 600):
                    game_framework.push_state(shop_state)

def update():
    global bg_posx
    global background_right
    global bg_move
    if bg_move:
        if(background_right and bg_posx > 100):
            bg_posx -= 20
        elif((not background_right) and bg_posx < 700):
            bg_posx += 20
        elif(bg_posx <= 100 or bg_posx >= 700):
            bg_move = False
    delay(0.01)


def draw():
    global bg_posx
    clear_canvas()
    background.draw(bg_posx, 300)
    if (not bg_move):
        button_battle.clip_draw(0, 0, 105, 35, 70, 17)
        button_shop.clip_draw(0, 0, 105, 35, 185, 17)
        button_room.clip_draw(0, 0, 105, 35, 295, 17)
    update_canvas()