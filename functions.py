import data
import random
import keyboard

def create_monster():
    name = random.choice(data.monsters)
    dmg = data.monster_dmg[name]
    hp = data.monster_hp[name]
    return name, dmg, hp

def fighting(hp1, dmg1, hp2, dmg2, monster_count):
    while hp1 > 0:
        hp2 -= dmg1 + random.randint(-10, 10)
        if hp2 > 0:
            hp1 -= dmg2 + random.randint(-5, 5)
        else:
            monster_count += 1
            if monster_count < 5:
                message_text = f'Ты победил врага!🎉 Твое здоровье: {hp1}' 
                markup = keyboard.win()
                hp1 = hp1 + random.randint(50, 100)
                return hp1, message_text, markup, monster_count
            else:
                message_text = 'Ты прошел игру!'
                markup = keyboard.game_over()
                return hp1, message_text, markup, monster_count
    else:
        message_text = 'Ты проиграл😢' 
        markup = keyboard.game_over()
        return hp1, message_text, markup, monster_count
    


     

