import game_framework
import tutorial
import prologue
from pico2d import *


name = "TitleState"
main_image = None
logo_image = None
title_bgm = None
#565
title_posy = 565
start = False

def enter():
    global main_image
    global logo_image
    global title_bgm
    main_image = load_image('bgi\\bg_title.png')
    logo_image = load_image('image\\tpw2nd_logo.png')
    title_bgm = load_music('bgm\\bgm_title2.ogg')
    title_bgm.repeat_play()


def exit():
    global main_image
    global logo_image
    global title_bgm
    del(main_image)
    del(logo_image)
    del(title_bgm)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if((event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE)) and start:
                game_framework.change_state(prologue)


def draw():
    global title_posy
    global start
    clear_canvas()
    main_image.draw(400, title_posy)
    if start:
        logo_image.draw(400, 300)
    update_canvas()


def update():
    global title_posy
    global start
    if title_posy > 35:
        title_posy -= 1.0
    else:
        start = True
    pass


def pause():
    pass


def resume():
    pass