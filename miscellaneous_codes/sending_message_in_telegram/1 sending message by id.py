# با فیلتر شکن کار میکنه.
# pip install pyTelegramBotAPI
import telebot
from my_token import MY_TOKEN
bot = telebot.TeleBot(MY_TOKEN)
chat_id = '84047486' # Madval1369
message = "خوبی؟"
bot.send_message(chat_id, message)