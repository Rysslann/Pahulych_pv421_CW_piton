import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6938585575:AAGY7j4iAgDL4jTRZgeHtKOYBeEG-7omoHI"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про проект")],
            [KeyboardButton(text="Реквізити"), KeyboardButton(text="Про мене")],
            [KeyboardButton(text="Про вас")]
        ],
        resize_keyboard=True
    )
    return kb


def r_who_you():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пес"), KeyboardButton(text="Норм чувак"),
             KeyboardButton(text="Затрудняюсь відповісти")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    return kb


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML", reply_markup=r_main_menu())


@dp.message()
async def special_msg(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text
    print("__test", content)
    print("__id", cid)

    if content == "/secret":
        await message.answer("You activeted secret modу. Which does nothing", reply_markup=ReplyKeyboardRemove())
    elif content == "Реквізити":
        await message.answer("<b>Кинь пару копійок</b>", parse_mode="HTML")
        await message.answer("<b>4441 1144 6869 9317</b>", parse_mode="HTML")
    elif content == "Про проект":
        await message.answer("Поки що він не робить нічого корисного")
    elif content == "Про мене":
        await message.answer("Норм чувак")
    elif content == "Про вас":
        await message.answer("А ви хто? Оберіть в під меню ↓", reply_markup=r_who_you())
    elif content == "Пес":
        await message.answer("Ти як сюда попав?")
    elif content == "Норм чувак":
        await message.answer("Є сумніви")
    elif content == "Затрудняюсь відповісти":
        await message.answer("Норм чувак")
    elif content == "Назад":
        await message.answer("Ви вернулись в головне меню ↓ ", reply_markup=r_main_menu())


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
