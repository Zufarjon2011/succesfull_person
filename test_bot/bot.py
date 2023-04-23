import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот, который может разговаривать с тобой. Напиши мне что-нибудь.")

# Обработчик сообщений пользователя
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Создаем объект бота и регистрируем обработчики команд и сообщений
updater = Updater(token='5855893186:AAG6SSYdyg-HjRVL2eO-uCRq-G5Li-K13gI', use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Запускаем бота
updater.start_polling()
updater.idle()
