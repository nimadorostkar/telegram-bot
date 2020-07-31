from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json

updater = Updater('Telegramm api key')



def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "salammm dooste aziz 🌹 , khosh oomadi {}  \n\n\n\n  /start--> salam\n /admin--> admin control \n /help--> help\n /info--> info".format(update.message.from_user.first_name))
    print(update)
    print("---------------")

def helper(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "help help help help help help help ")

def info(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "info info info info info info info  ")

def admin_control(bot, update):
    if (update.message.chat_id == 378089614 ):  # if (update.message.from_user.first_name == "@nimadorostkar" )
        bot.send_message(chat_id = update.message.chat_id , text = "✅ admin find ✅  ")
        bot.send_message(chat_id = update.message.chat_id , text = "✅ update !! ✅ ")
    else:
        bot.send_message(chat_id = update.message.chat_id , text = " ❌ error ❌ ")

def message_filter(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "شما گفتید : {}".format(update.message.text))



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helper))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CommandHandler('admin', admin_control))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_filter))

print("server is runing . . . ")

updater.start_polling()
updater.idle()
