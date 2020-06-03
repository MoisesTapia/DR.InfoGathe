# Token 1028080729:AAF0j1kMWeIkEy8Hi16fPSgiKAHLf-7IDt0
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

update = Updater(token="1028080729:AAF0j1kMWeIkEy8Hi16fPSgiKAHLf-7IDt0")


def helpp(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                    text='''use /start to start boot\nuse /option to see options\nuse /scann to scann any website\nuse /info to get more infor about creator''')

dispacher = update.dispatcher
helpp_handler= CommandHandler("help", helpp)
dispacher.add_handler(helpp_handler)
############################################################################################
def option(bot, update):
    button = [
        [InlineKeyboardButton("Port Scanning.", callback_data="1"),
         InlineKeyboardButton("Headers.", callback_data="2")],
        [InlineKeyboardButton("Best-Tools Of 2020.", callback_data="3"),
         InlineKeyboardButton("Donation. ", callback_data="4")]
    ]
    reply_markup=InlineKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id,
                    text="Choose one option",
                    reply_markup=reply_markup)

option_handler = CommandHandler("option", option)
dispacher.add_handler(option_handler)
###########################################################################################
def button(bot, update):
    query= update.callback_query

    bot.edit_message_text(chat_id=query.message.chat_id,
                    text="thanks for choose{}".format(query.data),
                    message_id=query.message.message_id)

button_handler = CallbackQueryHandler(button)
dispacher.add_handler(button_handler)
############################################################################################
def scann_ip(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                    text='''Enter the ip adress or url: ''')

dispacher = update.dispatcher
scann_handler= CommandHandler("scann", scann_ip)
dispacher.add_handler(scann_handler)
#############################################################################################
def info_bot(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
                    text="Nombre: Dr. InfoGhate\nCreator: Moises Tapia\nTeam: Dart-Security")

dispacher = update.dispatcher
info_handler= CommandHandler("info", info_bot)
dispacher.add_handler(info_handler)
##############################################################################################
# define command callback function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                    text="Welcome to Dr. InfoGhet\nGet more help with the command /help.")
#allos to regisrer handler
dispacher = update.dispatcher
# create a command handler
start_handler = CommandHandler("start", start)
#add command handler to dispatcher
dispacher.add_handler(start_handler)
###############################################################################################
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                    text=update.message.text.upper())
# create a text handler
dispacher = update.dispatcher
echo_handler = MessageHandler(Filters.text, echo)
dispacher.add_handler(echo_handler)
###############################################################################################
#start polling
update.start_polling()
