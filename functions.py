import data
import random

def create_monster():
    name = random.choice(data.monsters)
    dmg = data.monster_dmg[name]
    hp = data.monster_hp[name]
    return name, dmg, hp

def fighting(hp1, dmg1, hp2, dmg2):
    while hp1 > 0:
        hp2 -= dmg1
        if hp2 > 0:
            hp1 -=dmg2
        else:
            message_text = '' 
            markup = ''
            return hp1, message_text, markup
    else:
        message_text = '' 
        markup = ''
        return hp1, message_text, markup

     

