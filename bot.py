
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
from aiogram import F
from datetime import datetime
import time
from aiogram import html
from aiogram.utils.markdown import hide_link
from random import randint
from aiogram.filters import Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}")

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Здраствуйте! {message.from_user.full_name}")
    user_name = message.from_user.first_name
    for i in range(7):
        time.sleep(2)
    await message.answer(message.chat.id, text=f"Программировал ли  сегодня {user_name} ?")


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

# @dp.message()
# async def dice(message: types.Message):
#     await message.answer(message.text)
# @dp.message(F.text)
# async def time(message: types.Message):
#     time_now = datetime.now().strftime("%H:%M")
#     added_text = html.underline(f"Создано в {time_now}")
#     await message.answer(f"{message.text}\n\n{added_text}", parse_mode="HTML")

@dp.message(Command("hidden_link"))
async def hidden_link(message: types.Message):
    await message.answer(
        f"{hide_link('https://telegra.ph/file/562a512448876923e28c3.png')}"
        f"Домашка *существует*\n"
        f"Студенты: *не выполняют*\n"
        f"Я:"
    )

@dp.message(Command("reply_bulder"))
async def reply_bulder(message: types.Message):
    bulder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        bulder.add(types.KeyboardButton(text=str(i)))
    bulder.adjust(3)
    await message.answer(
        "Выберите число: ",
        reply_markup=bulder.as_markup(resize_keybord = True)
    )

@dp.message(Command("random"))
async def random (message: types.Message):
    bulder = InlineKeyboardBuilder()
    bulder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value"
    ))
    await message.answer(
        "Нажми на кнопку чтобы бот отправил тебе цифру от 1 до 10",
        reply_markup=bulder.as_markup()
    )

@dp.callback_query(Text("random_value"))
async def send_random_value(callbask: types.CallbackQuery):
    await callbask.message.answer(str(randint(1, 10)))

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

