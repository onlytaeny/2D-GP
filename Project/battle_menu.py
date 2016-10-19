import random
import json
import os

from pico2d import *

import game_framework
import prepare_battle

import Function

name = "battle_menu"

background = None
bg_normal = None
bg_cup = None
bg_duel = None

button_normal = None
button_duel = None
button_cup = None

stand_koakuma = None

select_menu = 0

def enter():
    global background
    global bg_normal
    global bg_cup
    global bg_duel
    global button_normal
    global button_duel
    global button_cup
    global stand_koakuma
    background = load_image('bgi\\bg_game.png')
    bg_normal = load_image('bgi\\bg_free_battle.png')
    bg_cup = load_image('bgi\\bg_cup_battle.png')
    bg_duel = load_image('bgi\\bg_duel_battle.png')
    button_normal = load_image('image\\button_menu_normal.png')
    button_duel = load_image('image\\button_menu_duel.png')
    button_cup = load_image('image\\button_menu_cup.png')
    stand_koakuma = load_image('csimage\\st_koakuma.png')


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
            elif((event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)):
                if Function.PointInRect(event.x, event.y, 0, 113, 51, 149):
                    select_menu = 1
                elif Function.PointInRect(event.x, event.y, 0, 113, 151, 249):
                    select_menu = 2
                elif Function.PointInRect(event.x, event.y, 0, 113, 251, 349):
                    select_menu = 3

                if select_menu == 1:
                    if Function.PointInRect(event.x, event.y, 125, 260, 130, 160):
                        game_framework.change_state(prepare_battle)
                        select_menu = 0


def update():
    pass


def draw():
    clear_canvas()
    background.draw(400, 300)
    if select_menu == 1:
        bg_normal.draw(400, 300)
    elif select_menu == 2:
        bg_cup.draw(400, 300)
    elif select_menu == 3:
        bg_duel.draw(400, 300)
    button_normal.clip_draw(0, 0, 113, 98, 56, 500)
    button_cup.clip_draw(0, 0, 113, 98, 56, 400)
    button_duel.clip_draw(0, 0, 113, 98, 56, 300)
    stand_koakuma.draw(650, 300)
    update_canvas()