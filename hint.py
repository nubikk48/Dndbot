import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6459858653:AAFGB9cj7PY9wiKGtIFEZfTtqLAvxb8PrD8') #подключение к боту

@bot.message_handler(commands = ['start' , 'help']) # @ - декоратор(проверочная функция)
def start_command(message):
    user_name = message.chat.first_name # имя пользователя
    user_id = message.chat.id
    text = (f"Приветсвую тебя, {user_name}!"
            f"Здесь ты можешь поиграть в РПГ игру. "
            f" Нажми на 'Начать игру' для запуска")
    
    start_keyboard = ReplyKeyboardMarkup()#murkup - объявление клавиатуры
    btn_random_int = KeyboardButton('Назови случайное число')
    start_keyboard.add(btn_random_int)
    btn_start_game = KeyboardButton('Начать игру')
    start_keyboard.add(btn_start_game)
    bot.send_message(chat_id = user_id, text = text, reply_markup = start_keyboard)
    # bot.send_message(chat_id = 1104818675, text = 'Bot starting')
    


@bot.message_handler(regexp = 'Назови случайное число')
def send_random_int(message):
    rand_int =str(random.randint(0, 100))
    user_id = message.chat.id
    bot.send_message(chat_id = user_id, text = rand_int)

@bot.message_handler(regexp = 'Начать игру')
def btn_start_game(message):
    greetings = str('Назови себя')
    user_id = message.chat.id
    bot.send_message(chat_id = user_id, text = greetings)

@bot.message_handler(commands = ['inline'])
def inline_command(message):
    markup = InlineKeyboardMarkup()
    #btn1 = InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    btn1 = InlineKeyboardButton(text='Кнопка один', callback_data ='1')
    btn2 = InlineKeyboardButton(text = 'Кнопка два', callback_data = '2')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выбери кнопку", reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def get_call_back(call):
    print(call)
    print(call.data)
    user_id = call.from_user.id
    message_id = call.message.message_id
    if call.data == '1':
        bot.send_message(chat_id = user_id, text = 'Ты выбрал первую кнопку')
    elif call.data == '2':
         bot.send_message(chat_id = user_id, text = 'Ты выбрал вторую кнопку')
    bot.delete_message(chat_id = user_id, message_id = message_id)

@bot.message_handler(content_types = ['text'])
# content_types=['audio', 'photo', 'voice', 'video', 'document',
# 'text', 'location', 'contact', 'sticker']
def repeat(message):
    print(message)
    print(message.chat.username)
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True) #бот работает пока не нажмем Ctrl + C