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

@bot.callback_query_handler(func=lambda call: True)
def get_call_back(call):
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
        bot.send_message(chat_id = user_id, 
                         text = f'Твоя раса: {call.data}, здоровье: {data.race_hp[call.data]}, урон: {data.race_dmg[call.data]}.',
                         reply_markup = markup)
    if call.data == 'choose_class': #выбор класса
        markup = keyboard.class_kb()
        bot.send_message(chat_id = user_id, 
                         text = f'Выбери класс, {user_name}!',
                         reply_markup = markup)
        
#ntcnjdjt bpvtytybt

 
bot.polling(non_stop=True)
