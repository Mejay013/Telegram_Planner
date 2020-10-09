import vk_api
from vk_api.longpoll import VkLongPoll,VkEventType
from datetime import datetime
import telebot
from telebot import types
import stock


bot = telebot.TeleBot(stock.token)

keyboard = types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start']) # вступителная функция
def start_message(message):
    key_event = types.InlineKeyboardButton(text='Добавить событие', callback_data='new_event')
    keyboard.add(key_event)
    bot.send_message(message.from_user.id, text='Выберите дейстиве', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True) #обработка кнопок
def callback_worker(call):
    if call.data == "new_event": 
        bot.send_message(call.message.chat.id, 'Новое действие')

@bot.message_handler(content_types=['text']) #обработка текстовых сообщений
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")



bot.polling()

