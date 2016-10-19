import random
import json
import os

from pico2d import *

import game_framework

import Function

name = "shop_state"

background = None
bg_avatar = None
bg_misc = None

button_gacha = None
button_card = None
button_avatar = None
button_misc = None

stand_mori = None

gacha = []
cardpack = []

select_menu = 0

def enter():
    global background
    global bg_avatar
    global bg_misc
    global button_gacha
    global button_card
    global button_avatar
    global button_misc
    global stand_mori
    background = load_image('bgi\\bg_shop.png')
    bg_avatar = load_image('bgi\\shop_avatar.png')
    bg_misc = load_image('bgi\\shop_goods.png')
    button_gacha = load_image('image\\button_menu_gacha.png')
    button_card = load_image('image\\button_menu_card.png')
    button_avatar = load_image('image\\button_menu_avatar.png')
    button_misc = load_image('image\\button_menu_misc.png')
    stand_mori = load_image('csimage\\st_mori.png')
    for i in range(1, 13):
        gacha.append(load_image('image\\gacha_' + str(i) + '.png'))
    for i in range(1, 6):
        cardpack.append(load_image('image\\cardpack_' + str(i) + '.png'))
    cardpack.append(load_image('image\\cardpack_99.png'))

def exit():
    global background
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global select_menu
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT)):
                if select_menu == 0:
                    game_framework.pop_state()
                else:
                    select_menu = 0
            elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                if Function.PointInRect(event.x, event.y, 0, 113, 51, 149):
                    select_menu = 1
                elif Function.PointInRect(event.x, event.y, 0, 113, 151, 249):
                    select_menu = 2
                elif Function.PointInRect(event.x, event.y, 0, 113, 251, 349):
                    select_menu = 3
                elif Function.PointInRect(event.x, event.y, 0, 113, 351, 449):
                    select_menu = 4

def update():
    pass


def draw():
    clear_canvas()
    background.draw(400, 300)
    button_gacha.clip_draw(0, 0, 113, 98, 56, 500)
    button_card.clip_draw(0, 0, 113, 98, 56, 400)
    button_avatar.clip_draw(0, 0, 113, 98, 56, 300)
    button_misc.clip_draw(0, 0, 113, 98, 56, 200)
    if select_menu == 0:
        stand_mori.draw(400, 300)
    elif select_menu == 1:
        for i in range(0, 3):
            gacha[i].clip_draw(0, 0, 172, 385, 300 + (180 * i), 300)
    elif select_menu == 2:
        for i in range(0, 5):
            cardpack[i].clip_draw(0, 0, 300, 150, 300 + (320 * (i % 2)), 435 - (155 * (i // 2)))
        cardpack[-1].clip_draw(0, 0, 300, 150, 620, 125)
    elif select_menu == 3:
        bg_avatar.draw(400, 300)
    elif select_menu == 4:
        bg_misc.draw(400, 300)

    update_canvas()