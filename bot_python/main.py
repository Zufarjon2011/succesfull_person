from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка Premium', 'Покупка Telegram Premium', 'invoice', config.PAYMENTS_TOKEN, 'USD', [types.LabeledPrice('Покупка Premium', 5*100)])

executor.start_polling(dp)