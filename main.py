import telebot
import tokenidtelegram
import requests

tokenidtelegram.init()
bot = telebot.TeleBot(tokenidtelegram.tokenid)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'эхо')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "твое сообщение"+ message.text)

bot.polling(none_stop=True, interval=0)

