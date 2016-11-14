import random
import json
import os

from pico2d import *

import game_framework

import Function

name = "battle"

background = None
battle_ui = None
button_set = None
button_act = None
button_charge = None
button_reset = None
down_arrow = None

enemy = None
enemy_assist = None
assist = None

select = []
my_doll = []
story = []
spell = []
tuto_atk = []
select_count = 0
story_count = 0
select_spell = 0
select_spell2 = 0

attack = False
ctrl_flag = 0
time_flag = 0

ypos = 500

def enter():
    global background
    global battle_ui, button_set, button_act, button_charge, button_reset, down_arrow
    global enemy
    global assist
    global enemy_assist
    background = load_image('bgi\\bg_battle_game.png')
    battle_ui = load_image('bgi\\bg_battle_up.png')
    button_set = load_image('image\\button_battle_set.png')
    button_act = load_image('image\\button_act.png')
    button_charge = load_image('image\\button_charge.png')
    button_reset = load_image('image\\button_reset.png')
    down_arrow = load_image('image\\danmaku_down.png')
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
    spell.append(load_image('image\\image_24_card06.png'))
    spell.append(load_image('image\\image_zako_card01.png'))
    spell.append(load_image('image\\image_zako_card02.png'))
    spell.append(load_image('image\\image_zako_card03.png'))
    spell.append(load_image('image\\image_44_card04.png'))
    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_1.name) + 'g.png'))
    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_2.name) + 'g.png'))
    spell.append(load_image('image\\' + str(my_doll[0][1].battle_spell_3.name) + 'g.png'))

    tuto_atk.append(load_image('image\\q_atk_38.png'))
    tuto_atk.append(load_image('image\\q_atk_44.png'))
    tuto_atk.append(load_image('image\\q_atk_mao.png'))



def exit():
    global background
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    global select_count, select_spell, select_spell2
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
                    elif story_count == 6:
                        story_count = 7
                        ctrl_flag = 2
                    elif story_count == 9:
                        ctrl_flag = 4
                    elif story_count == 11:
                        ctrl_flag = 5
                    elif story_count == 13:
                        ctrl_flag = 6
                    elif story_count == 14:
                        ctrl_flag = 9
                    elif story_count == 18:
                        ctrl_flag = 10
                    elif story_count < 21:
                        story_count += 1
                    elif story_count == 21:
                        game_framework.pop_state()

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
                    if story_count == 3:
                        for i in range(0, 3):
                            if Function.PointInRect(event.x, event.y, 117 + (i * 75), 183 + (i * 75), 518, 592):
                                select_spell = i
                                story_count += 1
                                ctrl_flag = 0
                                break

                elif ctrl_flag == 2:
                    if Function.PointInRect(event.x, event.y, 110 + (select_spell * 75), 190 + (select_spell * 75), 567, 597):
                        ctrl_flag = 3

                elif ctrl_flag == 4:
                    if Function.PointInRect(event.x, event.y, 10, 90, 567, 597):
                        ctrl_flag = 0
                        story_count += 1

                elif ctrl_flag == 6 or ctrl_flag == 7:
                    for i in range(0, 3):
                        if Function.PointInRect(event.x, event.y, 117 + (i * 75), 183 + (i * 75), 518, 592):
                            select_spell2 = i
                            ctrl_flag = 7
                            break

                    if ctrl_flag == 7 and Function.PointInRect(event.x, event.y, 110 + (select_spell2 * 75),
                                                               190 + (select_spell2 * 75), 567, 597):
                        ctrl_flag = 8

                elif ctrl_flag == 10:
                    if Function.PointInRect(event.x, event.y, 10, 90, 535, 565):
                        ctrl_flag = 0
                        story_count += 1


def update():
    global ypos, ctrl_flag, story_count, time_flag
    if (ctrl_flag == 3 or ctrl_flag == 5 or ctrl_flag == 8) and ypos > 300:
        ypos -= 1
    elif (ctrl_flag == 3 or ctrl_flag == 5 or ctrl_flag == 8) and ypos <= 300:
        delay(1)
        ctrl_flag = 0
        story_count += 1
        ypos = 500

    if ctrl_flag == 9:
        time_flag += 1
        if time_flag > 500:
            ctrl_flag = 0
            story_count += 1


def draw():
    global attack, ctrl_flag, select_spell, ypos
    clear_canvas()
    background.draw(400, 300)
    if select_count < 3 and ctrl_flag == 1:
        for i in range(0, 9):
            button_set.clip_draw(0, 0, 96, 32, 65 + (110 * (i % 3)), 235 - (45 * (i // 3)))
    if ctrl_flag == 3:
        tuto_atk[0].draw(65 + (110 * (select[0] % 3)), 350 - (45 * (select[0] // 3)))
        for i in range(1, select_count):
            my_doll[i][0].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
        spell[select_spell].clip_draw(0, 0, 65, 74, 625, ypos)
    elif ctrl_flag == 8:
        tuto_atk[1].draw(65 + (110 * (select[2] % 3)), 350 - (45 * (select[2] // 3)))
        for i in range(0, select_count - 1):
            my_doll[i][0].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
        spell[7].clip_draw(0, 0, 65, 74, 175, ypos)
    else:
        for i in range(0, select_count):
            my_doll[i][0].draw(65 + (110 * (select[i] % 3)), 350 - (45 * (select[i] // 3)))
    if ctrl_flag == 5:
        spell[4].clip_draw(0, 0, 65, 74, 175, ypos)
    battle_ui.draw(400, 300)
    if ctrl_flag == 9:
        down_arrow.draw(785, 135)
    if select_count == 3:
        assist.draw(52, 567)
        if 2 < story_count < 8 or 15 < story_count:
            for i in range(0, 3):
                spell[i].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
            if 15 < story_count:
                spell[select_spell + 8].clip_draw(0, 0, 65, 74, 150 + (select_spell * 75), 45)
        if ctrl_flag == 4:
            for i in range(0, 3):
                spell[3].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
            button_charge.clip_draw(0, 0, 80, 30, 50, 18)
        if ctrl_flag == 5:
            for i in range(0, 3):
                spell[i + 4].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
        if 5 < ctrl_flag < 9:
            for i in range(0, 3):
                spell[7].clip_draw(0, 0, 65, 74, 150 + (i * 75), 45)
    enemy.draw(735, 350)
    enemy.draw(625, 305)
    if ctrl_flag == 5:
        tuto_atk[2].draw(515, 260)
    else:
        enemy.draw(515, 260)
    enemy_assist.draw(750, 567)
    if not(ctrl_flag == 3) and not(ctrl_flag == 5) and not(ctrl_flag == 8) and not(ctrl_flag == 9):
        if ctrl_flag == 2:
            button_act.clip_draw(0, 0, 80, 30, 150 + (select_spell * 75), 18)
        if ctrl_flag == 7:
            button_act.clip_draw(0, 0, 80, 30, 150 + (select_spell2 * 75), 18)
        if 15 < story_count:
            button_reset.clip_draw(0, 0, 80, 30, 50, 50)
        if story_count < 2:
            story[story_count].draw(600, 210)
        elif story_count < 22:
            story[story_count].draw(200, 210)
    update_canvas()