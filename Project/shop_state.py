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
bg_unit_set = None

button_gacha = None
button_card = None
button_avatar = None
button_misc = None
button_get = None
button_drop = None
button_unit = None

stand_mori = None

dialog_gacha = None

random_doll = 5

gacha = []
cardpack = []

gacha_pack1 = []
char_pack1 = []

select_menu = 0

ctrl_flag = 0

def enter():
    global background, bg_avatar, bg_misc, bg_unit_set
    global button_gacha, button_card, button_avatar, button_misc, button_get, button_drop, button_unit
    global stand_mori
    global dialog_gacha
    background = load_image('bgi\\bg_shop.png')
    bg_avatar = load_image('bgi\\shop_avatar.png')
    bg_misc = load_image('bgi\\shop_goods.png')
    bg_unit_set = load_image('bgi\\bg_unit_set.png')
    button_gacha = load_image('image\\button_menu_gacha.png')
    button_card = load_image('image\\button_menu_card.png')
    button_avatar = load_image('image\\button_menu_avatar.png')
    button_misc = load_image('image\\button_menu_misc.png')
    button_unit = load_image('image\\button_unit_plinth.png')
    stand_mori = load_image('csimage\\st_mori.png')
    dialog_gacha = load_image('image\\dialog_gacha.png')
    button_get = load_image('image\\button_get.png')
    button_drop = load_image('image\\button_drop.png')
    for i in range(1, 13):
        gacha.append(load_image('image\\gacha_' + str(i) + '.png'))
    for i in range(1, 6):
        cardpack.append(load_image('image\\cardpack_' + str(i) + '.png'))
    cardpack.append(load_image('image\\cardpack_99.png'))
    gacha_pack1.append(load_image('image\\q_stand_3.png'))
    gacha_pack1.append(load_image('image\\q_stand_24.png'))
    gacha_pack1.append(load_image('image\\q_stand_38.png'))
    gacha_pack1.append(load_image('image\\q_stand_40.png'))
    gacha_pack1.append(load_image('image\\q_stand_43.png'))
    char_pack1.append(load_image('image\\border_3.png'))
    char_pack1.append(load_image('image\\border_24.png'))
    char_pack1.append(load_image('image\\border_38.png'))
    char_pack1.append(load_image('image\\border_40.png'))
    char_pack1.append(load_image('image\\border_43.png'))


def exit():
    global background
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global select_menu, random_doll, ctrl_flag
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if event.type == SDL_MOUSEBUTTONDOWN:
                print(event.x, event.y)
                print(ctrl_flag)
                if ctrl_flag == 0:
                    if event.button == SDL_BUTTON_RIGHT:
                        if select_menu == 0:
                            game_framework.pop_state()
                        else:
                            select_menu = 0
                    elif event.button == SDL_BUTTON_LEFT:
                        if Function.PointInRect(event.x, event.y, 0, 113, 51, 149):
                            select_menu = 1
                        elif Function.PointInRect(event.x, event.y, 0, 113, 151, 249):
                            select_menu = 2
                        elif Function.PointInRect(event.x, event.y, 0, 113, 251, 349):
                            select_menu = 3
                        elif Function.PointInRect(event.x, event.y, 0, 113, 351, 449):
                            select_menu = 4
                        if Function.PointInRect(event.x, event.y, 214, 386, 108, 492) and select_menu == 1:
                            random_doll = random.randint(0, 4)
                            ctrl_flag = 1
                elif ctrl_flag == 1:
                    if event.button == SDL_BUTTON_RIGHT:
                        ctrl_flag = 0
                        random_doll = 5
                    elif event.button == SDL_BUTTON_LEFT:
                        if Function.PointInRect(event.x, event.y, 480, 560, 395, 425):
                            ctrl_flag = 2
                        elif Function.PointInRect(event.x, event.y, 590, 670, 395, 425):
                            ctrl_flag = 0
                            random_doll = 5

def update():
    pass


def draw():
    global random_doll
    clear_canvas()
    if ctrl_flag < 2:
        background.draw(400, 300)
        button_gacha.clip_draw(0, 0, 113, 98, 56, 500)
        button_card.clip_draw(0, 0, 113, 98, 56, 400)
        button_avatar.clip_draw(0, 0, 113, 98, 56, 300)
        button_misc.clip_draw(0, 0, 113, 98, 56, 200)
        if select_menu == 0:
            stand_mori.draw(400, 300)
        elif select_menu == 1:
            for i in range(0, 1):
                gacha[i].clip_draw(0, 0, 172, 385, 300 + (180 * i), 300)
        elif select_menu == 2:
            for i in range(0, 5):
                cardpack[i].clip_draw(0, 0, 300, 150, 300 + (320 * (i % 2)), 435 - (155 * (i // 2)))
            cardpack[-1].clip_draw(0, 0, 300, 150, 620, 125)
        elif select_menu == 3:
            bg_avatar.draw(400, 300)
        elif select_menu == 4:
            bg_misc.draw(400, 300)
    elif ctrl_flag == 2:
        bg_unit_set.draw(400, 300)
        char_pack1[random_doll].clip_draw(0, 0, 800, 100, 400, 550)

    if ctrl_flag == 1:
        dialog_gacha.draw(400, 300)
        gacha_pack1[random_doll].draw(375, 300)
        button_get.clip_draw(0, 0, 80, 30, 520, 190)
        button_drop.clip_draw(0, 0, 80, 30, 610, 190)
    update_canvas()