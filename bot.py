from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton , InlineKeyboardMarkup , ReplyKeyboardMarkup
import requests
import json

updater = Updater('1094887685:AAFLLjhqPtR_IKER8crAlgx3qmYHl5rocVE')
start_text = "salaaaaaaaaaaaamm Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum "

#############################################################

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id ,
    text = " salam 🌹 , khosh oomadi {} ".format(update.message.from_user.first_name) + "\n\n\n" + start_text + "\n\n  /start--> salam\n  /livestream--> livestream\n /admin--> admin control \n ")

    print(update)
    print("---------------")

    keyboard0 = [
                [InlineKeyboardButton("livestream" , callback_data="01")],
                [InlineKeyboardButton("more info" , callback_data="02")]
               ]
    reply_markup0 = InlineKeyboardMarkup(keyboard0)
    update.message.reply_text("baraye edame mitoonid yeki ro entekhab konid :", reply_markup = reply_markup0)



def livestream(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "livestream livestream livestream livestream ")



################################################################3

def admin_control(bot, update):
    if (update.message.chat_id == 378089614 ):  # if (update.message.from_user.first_name == "@nimadorostkar" )
        bot.send_message(chat_id = update.message.chat_id , text = "✅ admin find ✅  ")
        bot.send_message(chat_id = update.message.chat_id , text = "✅ update ! ✅ ")

        #bot.send_message(chat_id = update.message.chat_id , text = textt)
        #reply_markup1 = InlineKeyboardMarkup(keyboard)
        #print(reply_markup1)
        #update.message.reply_text('Enter your details in the following format : Job Name;Phone Number;Email;Job Description')
        #print(update.message.text)

        keyboard = [

                    [InlineKeyboardButton("option 1" , callback_data="1")],
                    [InlineKeyboardButton("option 2" , callback_data="2")],
                    [InlineKeyboardButton("option 3" , callback_data="3")]

                   ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("lotfan yeki ro entekhab kon:", reply_markup = reply_markup)

    else:
        bot.send_message(chat_id = update.message.chat_id , text = " ❌ error ❌ ")


##############################################################################


def message_filter(bot, update):
    bot.send_message(chat_id = update.message.chat_id , text = "شما گفتید : {}".format(update.message.text))


def button(bot, update):
    query = update.callback_query
    print(query.data)

    if (query.data == "01"):
        bot.send_message(chat_id = query.message.chat_id , text = " livestream livestream  ✅ ")
        #livestream()


    elif (query.data == "02"):
        bot.send_message(chat_id = query.message.chat_id , text = " more info...  more info... more info... ")

    elif (query.data == "1"):
        bot.send_message(chat_id = query.message.chat_id , text = " option 1 ")




#########################################################################

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('livestream', livestream))
updater.dispatcher.add_handler(CommandHandler('admin', admin_control))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message_filter))


print("server is runing . . . ")

updater.start_polling()
updater.idle()
