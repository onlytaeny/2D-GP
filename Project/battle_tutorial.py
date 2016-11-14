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

enemy = None
enemy_assist = None
assist = None

select = []
my_doll = []
story = []
spell = []
select_count = 0
story_count = 0

attack = False
ctrl_flag = 0

def enter():
    global background
    global battle_ui
    global button_set
    global button_act
    global enemy
    global assist
    global enemy_assist
    background = load_image('bgi\\bg_battle_game.png')
    battle_ui = load_image('bgi\\bg_battle_up.png')
    button_set = load_image('image\\button_battle_set.png')
    button_act = load_image('image\\button_act.png')
    assist = load_image('image\\image_55.png')
    enemy = load_image('image\\q_stand_mao.png')
    enemy_assist = load_image('image\\image_mao.png')
    for i in range(50, 72):
        story.append(load_image('story\\tutorial\\K-' + str(i) + '.png'))
    my_doll.append([load_image('image\\q_stand_38.png'), Function.charactor('reimu')])
    my_doll.append([load_image('image\\q_stand_24.png'), Function.charactor('mari')])
    my_doll.append([load_image('image\\q_stand_44.png'), Function.charactor('sanae')])

    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_1.name) + '.png'))
    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_2.name) + '.png'))
    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_3.name) + '.png'))



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
    global story_count, ctrl_flag
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                print(event.x, event.y)
                print(story_count)
                if ctrl_flag == 0:
                    if story_count == 0 or story_count == 3:
                        ctrl_flag = 1
                    elif story_count < 50:
                        story_count += 1

                elif ctrl_flag == 1:
                    if select_count < 3:
                        for i in range(0, 9):
                            if Function.PointInRect(event.x, event.y, 17 + (110 * (i % 3)), 113 + (110 * (i % 3)),
                                                    349 + (45 * (i // 3)), 381 + (45 * (i // 3))):
                                select.append(i)
                                select_count += 1
                                if select_count == 3:
                                    ctrl_flag = 0
                                    story_count = 1
                                break
#                if Function.PointInRect(event.x, event.y, 260, 340, 597, 567):
#                    attack = True

#                print(attack)


def update():
    pass


def draw():
    global attack, ctrl_flag
    clear_canvas()
    background.draw(400, 300)
    if select_count < 3 and ctrl_flag == 1:
        for i in range(0, 9):
            button_set.clip_draw(0, 0, 96, 32, 65 + (110 * (i % 3)), 235 - (45 * (i // 3)))
    for i in range(0, select_count):
            my_doll[i][0].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
    battle_ui.draw(400, 300)
    if select_count == 3:
        assist.draw(52, 567)
        if story_count > 2:
            for i in range(0, 3):
                spell[i].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
    enemy.draw(735, 350)
    enemy.draw(625, 305)
    enemy.draw(515, 260)
    enemy_assist.draw(750, 567)
    if story_count < 2:
        story[story_count].draw(600, 210)
    elif story_count < 50:
        story[story_count].draw(200, 210)
    update_canvas()