import telegram

api_key = '785373685:AAGVIRlmpIiOzLZyftZkNnZFODxJQ6EdA9Q'

bot = telegram.Bot(token=api_key)

# chat_id = bot.get_updates()[-1].message.chat_id
chat_id = 166362247

bot.sendMessage(chat_id=chat_id, text='빵형, 안녕?')