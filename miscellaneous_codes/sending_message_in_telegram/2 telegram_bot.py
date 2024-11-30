# با فیلتر شکن کار میکنه.
# pip install pyTelegramBotAPI
import telebot

from my_token import MY_TOKEN

bot = telebot.TeleBot(MY_TOKEN)

@bot.message_handler(commands=['start', 'help', 'ok']) # لیست دستوراتی که با اسلش کار میکنند. /start /help /ok
def send_start(message):
    bot.reply_to(message, "به ربات من خوش آمدید.")

@bot.message_handler(func=lambda message: True) # لیست دستوراتی که مستقیم در چت مینویسیم.
def handle_message(message):
    text = message.text.lower()
    if text in ['salam', 'سلام']:
        bot.reply_to(message, "سلام داداچ. حالت چه طوره؟")
    elif text in ['bye', 'goodbye', 'khodanegahdar', 'خدانگهدار', 'خدا نگهدار', 'خداحافظ', 'خدا حافظ']:
        bot.reply_to(message, "از صحبت باهات خوشحال شدم. خدانگهدار.")
    else:
        bot.reply_to(message, "در حال حاضر فقط به چند مورد جواب میدهم. بقیه چیزها را مدیریت نکردم.")

bot.infinity_polling()