import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

# Укажите токен вашего бота
bot = Bot('7731154697:AAEjAcKgB4kSMUR6PDRk5w3PSxg763PGiBo')
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    # Создаем клавиатуру с выбором языка
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="O'zbek 🇺🇿", callback_data='set_lang_uz')],
        [types.InlineKeyboardButton(text="Русский 🇷🇺", callback_data='set_lang_ru')]
    ])

    await message.answer("Muloqot uchun tilni tanlang\n\nВыберите язык для общения", reply_markup=keyboard)

# Обработчик нажатия на кнопки выбора языка
@dp.callback_query(lambda callback_query: True)
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == 'set_lang_uz':
        await callback_query.answer("🇺🇿 O‘zbek tili tanlandi")
        await send_webpage_button(callback_query.message.chat.id, 'uz')
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    elif callback_query.data == 'set_lang_ru':
        await callback_query.answer("🇷🇺 Выбран русский язык")
        await send_webpage_button(callback_query.message.chat.id, 'ru')
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

# Функция отправки кнопки с веб-приложением
async def send_webpage_button(chat_id, lang):
    if lang == 'uz':
        text = "🎁 Oling 🎁"
        url = "https://clickuz.github.io/clickuz/test/uz.html"
    elif lang == 'ru':
        text = "🎁 Получить 🎁"
        url = "https://clickuz.github.io/clickuz/"

    # Создаем InlineKeyboardMarkup с кнопкой web_app
    markup = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text=text, web_app=types.WebAppInfo(url=url))]
    ])

    await bot.send_message(chat_id, 'Нажмите на кнопку 👇🏻\n\nTugmani bosing 👇🏻', reply_markup=markup)

# Основная функция запуска бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
