import random
import json

from pico2d import *

import game_framework
import main_state

import Function

name = "prologue"

black = None
bg_red1 = None
bg_lib = None
bg_human = None
story_bgm = None
story = []
story_count = 0
stand_reimu = None
stand_remi = None
stand_sakuya = None
stand_marisa = None
stand_aya = None
stand_hatate = None
stand_pachu = None

def enter():
    global black, story, bg_red1, bg_lib, bg_human
    global stand_reimu, stand_remi, stand_sakuya, stand_marisa, stand_aya, stand_hatate, stand_pachu
    global story_bgm
    black = load_image('bgi\\bg_black.png')
    bg_red1 = load_image('bgi\\bg_scn_red2.png')
    bg_lib = load_image('bgi\\bg_scn_library.png')
    bg_human = load_image('bgi\\bg_scn_human.png')
    stand_reimu = load_image('csimage\\st_reimu.png')
    stand_remi = load_image('csimage\\st_remi.png')
    stand_sakuya = load_image('csimage\\st_sakuya.png')
    stand_marisa = load_image('csimage\\st_marisa.png')
    stand_aya = load_image('csimage\\st_aya.png')
    stand_hatate = load_image('csimage\\st_hatate.png')
    stand_pachu = load_image('csimage\\st_pachu.png')
    story_bgm = load_music('bgm\\bgm_remi.ogg')
    for i in range(1, 87):
        story.append(load_image('story\\prologue\\K-' + str(i) + '.png'))


def exit():
    global black, story, bg_red1, bg_lib, bg_human
    global stand_reimu, stand_remi, stand_sakuya, stand_marisa, stand_aya, stand_hatate, stand_pachu
    global story_bgm
    del(black)
    del(story)
    del(bg_red1)
    del(bg_lib)
    del(bg_human)
    del(stand_reimu)
    del(stand_remi)
    del(stand_sakuya)
    del(stand_marisa)
    del(stand_aya)
    del(stand_hatate)
    del(stand_pachu)
    del(story_bgm)


def pause():
    pass


def resume():
    pass


def handle_events():
    global story_count
    global story_bgm
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)) and story_count < 85:
            story_count += 1
            print(story_count)
            if story_count == 2:
                story_bgm.repeat_play()
            if story_count == 15 or story_count == 47:
                story_bgm.stop()
            if story_count == 17:
                story_bgm = load_music('bgm\\bgm_pachu.ogg')
                story_bgm.repeat_play()
            if story_count == 48:
                story_bgm = load_music('bgm\\bgm_normal.ogg')
                story_bgm.repeat_play()
        elif ((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)) and story_count == 85:
            game_framework.change_state(main_state)
            Function.story_count = 1


def update():
    pass

def draw():
    global story_count
    clear_canvas()
    if story_count < 2 or story_count == 15 or story_count == 16 or story_count == 47:
        black.draw(400, 300)
    elif story_count < 15:
        bg_red1.draw(400, 300)
    elif story_count < 47:
        bg_lib.draw(400, 300)
    elif story_count < 86:
        bg_human.draw(400, 300)

    if story_count > 1:
        if story_count < 6:
            stand_reimu.draw(200, 300)
            stand_remi.draw(620, 300)
        elif story_count < 9:
            stand_marisa.draw(200, 300)
            stand_sakuya.draw(620, 300)
        elif story_count < 12:
            stand_aya.draw(200, 300)
            stand_hatate.draw(620, 300)
        elif story_count < 15 or 16 < story_count < 47:
            stand_pachu.draw(200, 300)
            stand_remi.draw(620, 300)
        elif 47 < story_count < 53:
            stand_aya.draw(400, 300)

    if story_count < 2:
        story[story_count].draw(400, 300)
    elif story_count < 86:
        story[story_count].draw(400, 40)
    update_canvas()