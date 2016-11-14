import random
import json

from pico2d import *

import game_framework
import battle_tutorial

name = "prologue"

ctrl_flag = False
tuto_bat_pre_count = 0

black = None
bg_red1 = None
bg_game = None
story = []
tutorial_battle = []
story_count = 0
stand_meirin = None
stand_koakuma = None
stand_remi = None
stand_kaguya = None
stand_sakuya = None
stand_yuyuko = None
stand_youmu = None
stand_yukari = None
stand_reimu = None
stand_marisa = None
doll_sakuya = None

def enter():
    global black, bg_red1, bg_game
    global stand_meirin, stand_koakuma, stand_remi, stand_kaguya, stand_sakuya, stand_yuyuko, stand_youmu, stand_yukari, stand_reimu, stand_marisa
    global doll_sakuya
    black = load_image('bgi\\bg_black.png')
    bg_red1 = load_image('bgi\\bg_scn_red.png')
    bg_game = load_image('bgi\\bg_scn_game.png')
    stand_meirin = load_image('csimage\\st_meirin.png')
    stand_koakuma = load_image('csimage\\st_koakuma.png')
    stand_remi = load_image('csimage\\st_remi.png')
    stand_kaguya = load_image('csimage\\st_kaguya.png')
    stand_sakuya = load_image('csimage\\st_sakuya.png')
    stand_yuyuko = load_image('csimage\\st_yuyuko.png')
    stand_youmu = load_image('csimage\\st_youmu.png')
    stand_yukari = load_image('csimage\\st_yukari.png')
    stand_reimu = load_image('csimage\\st_reimu.png')
    stand_marisa = load_image('csimage\\st_marisa.png')
    doll_sakuya = load_image('image\\q_stand_43.png')
    for i in range(1, 87):
        story.append(load_image('story\\tutorial\\K-' + str(i) + '.png'))
    for i in range(1, 6):
        tutorial_battle.append(load_image('bgi\\tutorial_battle_prepare0' + str(i) + '.png'))


def exit():
    global black, story
    del(black)
    del(story)


def pause():
    pass


def resume():
    pass


def handle_events():
    global story_count, ctrl_flag
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)) and story_count == 44:
            ctrl_flag = True
        if not ctrl_flag:
            if ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)) and story_count < 48:
                story_count += 1
                print(story_count)
            elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)) and story_count == 48:
                game_framework.push_state(battle_tutorial)


def update():
    global ctrl_flag, tuto_bat_pre_count, story_count
    if ctrl_flag and (tuto_bat_pre_count < 4):
        tuto_bat_pre_count += 1
        delay(1.0)
    elif tuto_bat_pre_count == 4 and story_count == 44:
        story_count = 45
        ctrl_flag = False

def draw():
    global story_count, tuto_bat_pre_count
    clear_canvas()
    if story_count < 5:
        bg_red1.draw(400, 300)
    elif story_count < 44:
        bg_game.draw(400, 300)
    elif story_count < 49:
        tutorial_battle[tuto_bat_pre_count].draw(400, 300)

    if story_count < 5:
        stand_meirin.draw(400, 300)
    elif 7 < story_count < 12 or 30 < story_count < 44:
        stand_koakuma.draw(400, 300)
    elif 11 < story_count < 16:
        stand_kaguya.draw(200, 300)
        stand_remi.draw(620, 300)
    elif 15 < story_count < 22:
        stand_sakuya.draw(620, 300)
        if 18 < story_count:
            stand_yuyuko.draw(200, 300)
        if 19 < story_count:
            stand_youmu.draw(400, 300)
    elif 21 < story_count < 26:
        stand_yukari.draw(400, 300)
    elif 25 < story_count < 30:
        stand_marisa.draw(200, 300)
        stand_reimu.draw(620, 300)

    if 34 < story_count < 44:
        doll_sakuya.draw(700, 230)

    if story_count < 49:
        story[story_count].draw(400, 40)
    update_canvas()