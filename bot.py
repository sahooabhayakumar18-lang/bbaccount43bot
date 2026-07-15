import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton(
        "🟢 100% Non-Used Code - ₹20",
        callback_data="buy20"
    )

    btn2 = InlineKeyboardButton(
        "🔵 90% Non-Used Code - ₹17",
        callback_data="buy17"
    )

    markup.add(btn1)
    markup.add(btn2)

    bot.send_message(
        message.chat.id,
        "👋 Welcome!\n\nPlease select a package:",
        reply_markup=markup
    )

bot.infinity_polling()
