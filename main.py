import telebot 
bot = telebot.TeleBot('6838465066:AAE2Xxe6biMp8jQRb4ruA_peUAUGAs64-6U')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет! \n\nвведи /cmds для вывода списка команд')

@bot.message_handler(commands=['balance'])
def main1(message):
    bot.send_message(message.chat.id, 'чтобы я показал тебе баланс, ты должен ввести данные с карточки твоей мамы. введи /instruction, если уж очень хочется, но не понимаешь как')

@bot.message_handler(commands=['instruction'])
def main2(message):
    bot.send_message(message.chat.id, ' *шестнадцать* цифр ты вводи \nпотом посмотрим что внутри \nнужна нам дата: *месяц*, *год* \nеще *три цифры* и джекпот', parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def main3(message):
    bot.send_message(message.chat.id, 'помоги мне купить молоко!')   

@bot.message_handler(commands=['cmds'])
def main(message):
    bot.send_message(message.chat.id, '/start - приветствие \n/balance - проверка баланса\n/help - кто из нас помощник?')



bot.infinity_polling()