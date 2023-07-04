# import telebot
# import random
# # Создание объекта бота и передача токена вашего бота
# bot = telebot.TeleBot('6332970563:AAGzR0YXgZcuxF1LGxUpiHIv_fl7w0j74-4')
# # Обработка команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет! Я телеграм-бот календарь.')
# @bot.message_handler(commands=['about'])
# def about(message):
#     bot.send_message(message.chat.id, 'Данный бот создан от @zufar_BRO, сейчас бот на разработке')
# @bot.message_handler(commands=['startgame'])
# def gamee(message):
#     bot.send_message(message.chat.id, 'Выберите число 1 до 5')
#     min_num = 1
#     max_num = 5
#     secret_num = random.randint(min_num, max_num)
#     message = int(input("число от {} до {}".format(min_num, max_num)))
#     if message.chat.id > secret_num:
#         bot.send_message(message.chat.id, 'Веденный число больше!')
#     elif message.chat.id < secret_num:
#         bot.send_message(message.chat.id, 'Веденный число меньше!')
#     else:
#         bot.send_message(message.chat.id, 'вы нашли число!')
import random
import telebot

# Создаем экземпляр бота и передаем токен вашего бота
bot = telebot.TeleBot('6289232063:AAGQM9xU9vLrdZm4e6EyxgYfRGR0qADwXhA')

# Функция-обработчик команды /start
@bot.message_handler(commands=['startgame'])
def start(message):
    bot.send_message(message.chat.id, "Я загадал число от 1 до 10 попрогуй угадать!!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте на бот 'Угадай число'!\n /startgame для старта игры!")

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, "Привет я бот угадай число мой разработчик @zufar_BRO\nесли вам грустно или скучно то играйте на этом боте!")

# Функция-обработчик сообщений с числом
@bot.message_handler(func=lambda message: True)
def guess_number(message):
    try:
        user_number = int(message.text)
        random_number = random.randint(1, 10)

        if user_number == random_number:
            bot.send_message(message.chat.id, "Поздравляю, ты угадал число!👏👏")
        elif user_number < random_number:
            bot.send_message(message.chat.id, "Загаданное число больше!")
        else:
            bot.send_message(message.chat.id, "Загаданное число меньше!")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите число!")

# Запускаем бота
bot.polling()