import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6938585575:AAGY7j4iAgDL4jTRZgeHtKOYBeEG-7omoHI"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


# REPLY KEYBORD
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍🎨Про проєкт")],
            [KeyboardButton(text="Реквізити"), KeyboardButton(text="План занять")],
            [KeyboardButton(text='Контакти')]
        ],
        resize_keyboard=True
    )
    return kb


def r_sub_contacts():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Соц. мережі"), KeyboardButton(text="Телефон")],
            [KeyboardButton(text='Назад')]
        ],
        resize_keyboard=True
    )


# INLAINE KAYBORD
def i_plan_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python Core", callback_data="plan_python_core")],
            [InlineKeyboardButton(text="HTML & CSS", callback_data="plan_html_css")],
            [InlineKeyboardButton(text="NEXT. js 14", callback_data="plan_next14"),
            InlineKeyboardButton(text="Контакти", callback_data="plan_contacts")]
        ]
    )

@dp.callback_query(lambda c: c.data)
async  def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    if data == "plan_python_core":
        # await bot.send_message(cid, text="Python Core")
        await bot.edit_message_text(
            text="Programe Python: https://www.olx.ua/uk/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_html_css":
        # await bot.send_message(cid, text="HTML & CSS")
        await bot.edit_message_text(
            text="HTML & CSS: https://www.olx.ua/uk/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_next14":
        # await bot.send_message(cid, text="NEXT. js 14")
        await bot.edit_message_text(
            text="NEXT. js 14: https://www.olx.ua/uk/",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_plan_menu(),
            disable_web_page_preview=True
        )
    elif data == "plan_contacts":
        # await bot.send_message(cid, text="NEXT. js 14")
        await bot.delete_message(chat_id=cid, message_id=msg_id)
        await bot.send_message(cid, "Ви відкрили контакти", reply_markup=r_sub_contacts())

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=r_main_menu(), )


@dp.message()
async def special_msg(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text

    # commands
    if content == "/hide":
        await message.answer("You activated secret mode!", reply_markup=ReplyKeyboardRemove())

    # btn
    if content == "Реквізити":
        await message.answer("""
        <b>Найменування отримувача:</b> ФОП Лялюк Ігор Романович
<b>Код отримувача:</b> 3618507015
<b>Рахунок отримувача:</b> UA953052990000026005041024474
<b>Назва банку:</b> АТ КБ "ПРИВАТБАНК"
        """, parse_mode="HTML")
    elif content == "Контакти":
        await message.answer("Ви в під меню -- Контакти --", reply_markup=r_sub_contacts())
    elif content == "Назад":
        await message.answer("Ви в головному меню!", reply_markup=r_main_menu())
    elif content == "План занять":
        await message.answer("Оберіть модуль курсу", reply_markup=i_plan_menu())

@dp.message()
async def special_commands(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
