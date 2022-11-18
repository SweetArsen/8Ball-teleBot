import telebot
from random import *

bot = telebot.TeleBot('5634200901:AAH3YTA0JYT6qo4aNbgSCkyWEPW5GCp00pk')

answers_for_bot = ('Yes', 'No', 'Maybe')

@bot.message_handler(commands=['start'])
def start(message):
    Chel = f'Greetings, <b>{message.from_user.first_name}</b>. What you would like to ask me?'
    bot.send_message(message.chat.id, Chel, parse_mode='html')
@bot.message_handler()
def answering(message):
    if '?' in message.text:
        bot.send_message(message.chat.id, choice(answers_for_bot), parse_mode='html')
    else:
        bot.send_message(message.chat.id, "It's not a question. Please add the symbol - [?] to the question.", parse_mode='html')
bot.polling(none_stop=True)