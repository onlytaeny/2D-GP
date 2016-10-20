slot = 1
max_slot = 1
doll_count = 0
dolls = []

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
        self.battle_num = 0

class spell:
    def __init__(self, name, ld, md, sd, cri, hit, mp):
        self.name = name
        self.long_damage = ld
        self.middle_damage = md
        self.short_damage = sd
        self.critical = cri
        self.hit = hit
        self.mp = mp

class charactor:
    def __init__(self, name):
        self.wife = False
        self.feel = 0
        self.enemy = 500
        self.battle_num = 0
        if name == "reimu":
            self.num = 38
            self.battle_spell_1 = spell("영부「몽상봉인」", 50, 50, 0, 0, 0, 14)
            self.battle_spell_2 = spell("영부「음양보옥」", 0, 50, 70, 20, 0, 26)
            self.battle_spell_3 = spell("영부「변환어폐」", 60, 60, 60, 10, 10, 52)
            self.assist_type = "def"
            self.assist_chance = 50
            self.assist_style = "atk"
            self.assist_value = 10

        if name == "remi":
            self.num = 40
            self.battle_spell_1 = spell("image_40_card01", 0, 70, 30, 0, 0, 14)
            self.battle_spell_2 = spell("image_40_card02", 80, 60, 0, 0, -10, 12)
            self.battle_spell_3 = spell("image_40_card03", 120, 40, 0, 10, 0, 38)
            self.assist_type = "atk"
            self.assist_chance = 25
            self.assist_style = "cri"
            self.assist_value = 20

        if name == "saku":
            self.num = 43
            self.battle_spell_1 = spell("절기「화려한 춤」", 0, 0, 100, 40, 0, 30)
            self.battle_spell_2 = spell("비도「실버 아트」", 20, 60, 70, 25, -5, 29)
            self.battle_spell_3 = spell("비도「페이크 일루전」", 50, 100, 0, 0, 10, 40)
            self.assist_type = "atk"
            self.assist_chance = 100
            self.assist_style = "hit"
            self.assist_value = 5

        if name == "mari":
            self.num = 24
            self.battle_spell_1 = spell("유성「메테오 샤워」", 0, 70, 30, 15, -5, 14)
            self.battle_spell_2 = spell("혜성「갤럭스 로커스」", 70, 30, 0, 0, 10, 24)
            self.battle_spell_3 = spell("마부「마스터 스파크」", 120, 60, 30, 10, -5, 44)
            self.assist_type = "atk"
            self.assist_chance = 20
            self.assist_style = ["cri", "mp"]
            self.assist_value = [20, 5]

remi = charactor('remi')
saku = charactor('saku')
reimu = charactor('reimu')
mari = charactor('mari')

dolls.append(Doll(remi, 65, 45, 41, 43, 46, 52, 8, 50000))
doll_count += 1
dolls.append(Doll(saku, 57, 17, 72, 48, 39, 56, 14, 50000))
doll_count += 1
dolls.append(Doll(reimu, 35, 25, 85, 54, 42, 35, 9, 50000))
doll_count += 1
dolls.append(Doll(mari, 55, 54, 51, 56, 24, 33, 8, 50000))
doll_count += 1