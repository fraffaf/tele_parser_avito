import telebot

bot = telebot.TeleBot('5215163849:AAGbR2D4qKH7iYUmQNUuBxS3S3Gh30hCuLI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'эхо')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, "твое сообщение"+ message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)