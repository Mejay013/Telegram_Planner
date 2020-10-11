from datetime import datetime
import telebot
from telebot import types
import stock
from Event import Event


bot = telebot.TeleBot(stock.token)
keyboard = types.InlineKeyboardMarkup()
event = None

def send_message(user_id, text, check_keyboard = False):
    global bot, keyboard
    if check_keyboard != False:
        bot.send_message(user_id,text = text, reply_markup=keyboard)
    else:
        bot.send_message(user_id,text = text)


@bot.message_handler(commands=['start']) # вступителная функция
def start_message(message):
    set_keyboard()
    send_message(message.from_user.id, 'Выберите действие', True) 

@bot.callback_query_handler(func=lambda call: True) #обработка кнопок
def callback_worker(call):
    global event
    if call.data == "new_event":
        event = 'new_event'
        send_message(call.message.chat.id, 'Введите событие \n Пример 13.10/Новая задача/17:40/18:40')
    
def create_events(date,task_name,time_start,time_end):
    event = Event()
    event.create_event(date,task_name,time_start,time_end)

def set_keyboard():
    global keyboard
    key_event = types.InlineKeyboardButton(text='Добавить событие', callback_data='new_event')
    keyboard.add(key_event)


@bot.message_handler(content_types=['text']) #обработка текстовых сообщений
def get_text_messages(message):
    if event != None and message.from_user.id == stock.my_id:
        if event == 'new_event':
            date,task_name,time_start,time_end = message.text.split('/')
            create_events(date,task_name,time_start,time_end)
            send_message(message.from_user.id, 'Событие создано! \n Выберите дальнейшее действие', True)



bot.polling()

