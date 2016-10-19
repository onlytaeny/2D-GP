from pico2d import *

def PointInRect(mx, my, left, right, bottom, top):
    if(mx < right and mx > left and my < top and my > bottom):
        return True
    else:
        return False

class Doll:
    def __init__(self, type, mp, rev, hp, atk, hit, dod, spd, heart):
        self.type = type
        self.mp = mp
        self.rev = rev
        self.hp = hp
        self.atk = atk
        self.hit = hit
        self.dod = dod
        self.spd = spd
        self.heart = heart
        self.remake = 0
        self.level = 1
        self.item = 0
        self.mastery = 0
        self.pos = 0

    def load_images(self):
        self.doll_image = load_image('image\\q_stand_' + str(self.type) + '.png')