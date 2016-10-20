import random
import json
import os

from pico2d import *

import game_framework

import battle_result

import Function

name = "battle"

background = None
battle_ui = None
button_set = None
button_act = None

test = None
assist = None

spell = []
select = []
my_doll = []
my_doll_atk = []
select_count = 0

attack = False

def enter():
    global background
    global battle_ui
    global button_set
    global button_act
    global test
    global assist
    background = load_image('bgi\\bg_battle_red2.png')
    battle_ui = load_image('bgi\\bg_battle_up.png')
    button_set = load_image('image\\button_battle_set.png')
    button_act = load_image('image\\button_act.png')
    test = load_image('image\\q_stand_24.png')
    spell.append(load_image('image\\' + str(Function.remi.battle_spell_1.name) + '.png'))
    spell.append(load_image('image\\' + str(Function.remi.battle_spell_2.name) + '.png'))
    spell.append(load_image('image\\' + str(Function.remi.battle_spell_3.name) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 1:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))
            my_doll_atk.append(load_image('image\\q_atk_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 2:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))
            my_doll_atk.append(load_image('image\\q_atk_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 3:
            my_doll.append(load_image('image\\q_stand_' + str(Function.dolls[i].type.num) + '.png'))
            my_doll_atk.append(load_image('image\\q_atk_' + str(Function.dolls[i].type.num) + '.png'))

    for i in range(0, Function.doll_count):
        if Function.dolls[i].battle_num == 4:
            assist = load_image('image\\image_' + str(Function.dolls[i].type.num) + '.png')



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
            if((event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)):
                game_framework.change_state(battle_result)
            if((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                print(event.x, event.y)
                if Function.PointInRect(event.x, event.y, 260, 340, 597, 567):
                    attack = True

                for i in range(0, 9):
                    if Function.PointInRect(event.x, event.y, 17 + (110 * (i % 3)), 113 + (110 * (i % 3)),
                                            349 + (45 * (i // 3)), 381 + (45 * (i // 3))) and select_count < 3:
                        select.append(i)
                        select_count += 1
                print(attack)


def update():
    pass


def draw():
    global attack
    clear_canvas()
    background.draw(400, 300)
    if select_count < 3:
        for i in range(0, 9):
            button_set.clip_draw(0, 0, 96, 32, 65 + (110 * (i % 3)), 235 - (45 * (i // 3)))
    for i in range(0, select_count):
        if attack:
            my_doll_atk[i].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
  #          attack = False
        else:
            my_doll[i].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
    battle_ui.draw(400, 300)
    if select_count == 3:
        assist.draw(52, 567)
        for i in range(0, 3):
            spell[i].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
        button_act.clip_draw(0, 0, 80, 30, 300, 18)
    test.draw(735, 350)
    test.draw(625, 305)
    test.draw(515, 260)
    update_canvas()