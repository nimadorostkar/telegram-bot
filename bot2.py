from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup


updater = Updater('telegram api key')
livestream = open("livestream.txt", "r")
livestream_text = livestream.read()

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id ,
    text = " سلام {} ".format(update.message.from_user.first_name) + "\n  به ربات رویال۹۰ خوش آمدید 🌹   \n شما همواره می توانید لینک پخش زنده بازیهای فوتبال از تمامی لیگ های دنیا را دریافت کنید .  \n\n /start--> salam\n  /info--> more info ")


    keyboard0 = [
                [InlineKeyboardButton("livestream" , callback_data="01")]
               ]
    reply_markup0 = InlineKeyboardMarkup(keyboard0)
    update.message.reply_text("برای این منظور لطفا کلید livestream را انتخاب کنید 👇", reply_markup = reply_markup0)


def info(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = " info info info ")


def button(bot, update):
    query = update.callback_query

    if (query.data == "01"):
        bot.send_message(chat_id = query.message.chat_id , text = livestream_text )


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('info', info))
updater.dispatcher.add_handler(CallbackQueryHandler(button))


print("server is runing . . . ")
updater.start_polling()
updater.idle()
