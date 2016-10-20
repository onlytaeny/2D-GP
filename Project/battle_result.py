import random
import json
import os

from pico2d import *

import game_framework

import Function

name = "battle_result"

background = None

bonus_item = None

my_doll = []

def enter():
    global background
    global bonus_item
    background = load_image('bgi\\bg_battle_result.png')
    bonus_item = load_image('image\\bonus_item_q.png')
    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 1:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 2:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 3:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 4:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))


def exit():
    global background
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global select_count
    global attack
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                print(event.x, event.y)


def update():
    pass


def draw():
    global attack
    clear_canvas()
    background.draw(400, 300)
    for i in range(0, 6):
        bonus_item.draw(75 + (i * 130), 160)
    for i in range(0, 4):
        my_doll[i].draw(95 + (i * 200), 440)
    update_canvas()