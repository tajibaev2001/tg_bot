
import logging
import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from conflig import TOKEN
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}")

@dp.message(Command("hi"))
async def start(message: types.Message):
    await message.answer('Hi!')

@dp.message(Command("dice"))
async def dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.FOOTBALL)

@dp.message(Command("special_buttonn"))
async def special_button(massage: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Отправка номера", request_contact = True),
        types.KeyboardButton(text="Отправка гелокации", request_location=True),

    )
    builder.row(types.KeyboardButton(
        text="Создать викторину",
        request_poll = types.KeyboardButtonPollType(type="quiz")

    ))

    await massage.answer(
        "Выберите дейстия: ",
        reply_markup=builder.as_markup(resize_keyboard = True)
    )
@dp.message(Command("inline_button"))
async def inline_button(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com/"
    ))
    builder.row(types.InlineKeyboardButton(
        text="Telegram",
        url="tg://resolve?domain=telegram"
    ))
    
    user_id = 1388785377
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(types.InlineKeyboardButton(
            text="Какой-то пользователь",
            url=f"tg://user?id={user_id}"
        ))
    
    await message.answer(
        "Выберите ссылку",
        reply_markup=builder.as_markup(),
    )

@dp.message(Command('id'))
async def id(message: types.Message):   
    await message.answer(message.from_user.id)

@dp.message()
async def dice(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

