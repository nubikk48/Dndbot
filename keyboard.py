from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import data
bot = telebot.TeleBot('6459858653:AAFGB9cj7PY9wiKGtIFEZfTtqLAvxb8PrD8')

def start_game():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Начать игру', callback_data ='start_game')
    markup.add(btn)
    return markup

def race_kb():
    markup = InlineKeyboardMarkup()
    races = data.races
    for race in races:
        btn = InlineKeyboardButton(text = race, callback_data = race)
        markup.add(btn)    
    return markup

def raceback_kb():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text = 'Выбрать другую расу', callback_data = 'start_game')
    btn2 = InlineKeyboardButton(text = 'Выбрать класс', callback_data = 'choose_class')
    markup.add(btn2)
    markup.add(btn1)
    return markup
 
def class_kb():
    markup = InlineKeyboardMarkup()
    classes= data.classes
    for classe in classes:
        btn = InlineKeyboardButton(text = classe, callback_data = classe)
        markup.add(btn)    
    return markup

def confrim_start():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text = 'Выбрать другой класс', callback_data = 'choose_class')
    btn2 = InlineKeyboardButton(text = 'Продолжить', callback_data = 'confrim_start')
    btn3 = InlineKeyboardButton(text = 'Начать сначала', callback_data = 'start_game')
    markup.add(btn2)
    markup.add(btn1)
    markup.add(btn3)
    return markup

def begining_fght():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text = 'Начать сражение🩸', callback_data = 'fight')
    btn2 = InlineKeyboardButton(text = 'Отказаться😨', callback_data = 'confrim_start')
    markup.add(btn1)
    markup.add(btn2)
    return markup

def game_over():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text = 'Начать сначала?', callback_data = 'start_game')
    markup.add(btn1)
    return markup
def win():
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text = 'Продолжить приключение?', callback_data = 'confrim_start')
    btn2 = InlineKeyboardButton(text ='Закончить приключение', callback_data = 'start_game')
    markup.add(btn1)
    markup.add(btn2)
    return markup





