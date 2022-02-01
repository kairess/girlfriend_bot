from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize

updater = Updater(token='785373685:AAGVIRlmpIiOzLZyftZkNnZFODxJQ6EdA9Q')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
  text = update.message.text
  chat_id = update.message.chat_id
  
  if '/start' in text:
    bot.send_message(chat_id=chat_id, text='Hello there.')
  elif '2' in text:
    bot.send_message(chat_id=chat_id, text=emojize('Sorry I can't understand:heart_eyes:', use_aliases=True))
  elif 'Owner' in text:
    bot.send_message(chat_id=chat_id, text='This is my Owner >> @XFlick')
  elif '0' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/mj.jpg', 'rb'))
  else:
    bot.send_message(chat_id=chat_id, text='Love you')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
