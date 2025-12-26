import os
import random
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

fals = [
    "امروز شانس با تو یاره 🌟",
    "یه خبر خوب در راهه 📩",
    "به هدفت خیلی نزدیک شدی ⏳",
    "صبر کن، نتیجه خوبه 🤍",
    "یه تغییر مثبت تو راهه 🌱"
]

def start(update, context):
    update.message.reply_text("سلام 🌙\nبرای فال دستور /fal رو بفرست")

def fal(update, context):
    update.message.reply_text(random.choice(fals))

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("fal", fal))

updater.start_polling()
updater.idle()
