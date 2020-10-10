from datetime import datetime
import telebot
from telebot import types
import stock
from Event import Event


bot = telebot.TeleBot(stock.token)
keyboard = types.InlineKeyboardMarkup()

event = None

@bot.message_handler(commands=['start']) # вступителная функция
def start_message(message):
    key_event = types.InlineKeyboardButton(text='Добавить событие', callback_data='new_event')
    keyboard.add(key_event)
    bot.send_message(message.from_user.id, text='Выберите дейстиве', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True) #обработка кнопок
def callback_worker(call):
    global event
    if call.data == "new_event":
        event = 'new_event'
        bot.send_message(call.message.chat.id, 'Введите событие \n Пример 13.10/Новая задача/17:40/18:40')
        

def create_event(date,task_name,time_end,time_start):
    event = Event()
    event.create_event(date,task_name,time_end,time_start)
    print()


@bot.message_handler(content_types=['text']) #обработка текстовых сообщений
def get_text_messages(message):
    print(event)
    if event != None:
        if event == 'new_event':
            date,task_name,time_start,time_end = message.text.split('/')
            print(date,task_name,time_end,time_start)



bot.polling()

