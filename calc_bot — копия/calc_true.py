import telebot

bot = telebot.TeleBot('6251180951:AAG_y10vzYRJzGh2sLFGBJnFXGAe_NoEvdc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я калькулятор бот.Мой создатель @ppp772. Введите выражение, которое нужно вычислить.')

@bot.message_handler(commands=['about'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! этого бота создали @ppp772 и @zufar_BRO. Бот создан 2023г 18 апреля!')
    
@bot.message_handler(content_types=['text'])
def calculate(message):
    try:
        result = eval(message.text)
        bot.send_message(message.chat.id, 'Результат: ' + str(result))
    except:
        bot.send_message(message.chat.id, 'Ошибка! Некорректное выражение, можете спрошыть об этом ошыбке от тех поддержки: @zufar_BRO ')

