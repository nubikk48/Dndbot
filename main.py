import telebot
import data
import keyboard
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6459858653:AAFGB9cj7PY9wiKGtIFEZfTtqLAvxb8PrD8') #подключение к боту

@bot.message_handler(commands = ['start' , 'help']) # @ - декоратор(проверочная функция)
def start_command(message):
    user_name = message.chat.first_name # имя пользователя
    user_id = message.chat.id
    text_message = (f"Приветсвую тебя, {user_name}!"
            f"Здесь ты можешь поиграть в РПГ игру. "
            f" Нажми на 'Начать игру' для запуска")   
    markup = keyboard.start_game()
    bot.send_message(user_id, text_message, reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True) #декоратор срабатывает после нажатия inline кнопки
def get_call_back(call):
    global user_name, user_hp, user_dmg, user_race, user_class

    user_id = call.from_user.id
    user_name = call.from_user.first_name
    message_id = call.message.message_id
    bot.delete_message(chat_id = user_id, message_id = message_id)
    if call.data == 'start_game': #выбор расы
        markup = keyboard.race_kb()
        bot.send_message(chat_id = user_id, 
                         text = 'Приветсвую тебя, игрок. Выбери расу: ',
                          reply_markup = markup)
    elif call.data in data.races: #сообщение с подтверждением расы
        markup = keyboard.raceback_kb()
        user_race = call.data
        user_hp = data.race_hp[call.data]
        user_dmg = data.race_dmg[call.data]
        bot.send_message(chat_id = user_id, 
                         text = f'Твоя раса: {user_race}, здоровье: {user_hp}, урон: {user_dmg}.',
                         reply_markup = markup)
    if call.data == 'choose_class': #выбор класса
        markup = keyboard.class_kb()
        bot.send_message(chat_id = user_id, 
                         text = f'Выбери класс, {user_name}!',
                         reply_markup = markup)
    elif call.data in data.classes:
        markup = keyboard.confrim_start()
        user_class = call.data
        user_hp = data.class_hp[call.data] + data.race_hp[user_race]
        user_dmg = data.class_dmg[call.data] + data.race_dmg[user_race]
        bot.send_message(chat_id = user_id, 
                         text = f'Твой класс: {user_class}, здоровье: {user_hp}, урон: {user_dmg}.',
                         reply_markup = markup)

        


 
bot.polling(non_stop=True)
