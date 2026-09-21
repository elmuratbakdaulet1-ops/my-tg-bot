import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен берём из переменной окружения (безопасно)
TOKEN = os.getenv("8875610425:AAGylX-48pNYa477jOZ2DiKvl-b82LV3xdY")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот. Напиши мне что-нибудь, и я повторю.")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Просто отправь текст — я его повторю.")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
