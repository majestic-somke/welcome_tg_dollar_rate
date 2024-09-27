import telebot
from env_loader import eloader
from api_requests import get_usd_rub


TG_TOKEN = eloader.get_var("TG_TOKEN")
bot = telebot.TeleBot(TG_TOKEN)
users = {}
dollar_rate = get_usd_rub() if get_usd_rub() else "неизвестен ¯\_(ツ)_/¯ "


@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id

    if chat_id not in users:
        users[chat_id] = {"name": ""}

    bot.send_message(chat_id, f"Добрый день. Как вас зовут?")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    chat_id = message.chat.id

    if chat_id in users and not users[chat_id].get("name"):
        users[chat_id] = {"name": message.text}

        bot.send_message(chat_id, f"Рад знакомству, {users[chat_id]['name']}! Курс доллара сегодня {dollar_rate}р")
    else:
        bot.send_message(chat_id, f"¯\_(ツ)_/¯")


bot.polling()
