from aiogram import Bot, executor
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message

PROXY_URL = 'http://proxy.server:3128'
TOKEN = '7190621333:AAGk6ReUvuWbDN2XNOpkdAMiEOAebnIp2Lg'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

CHANNEL_ID = -1002019991143

@dp.message_handler(commands=['start'])
async def handler_start(message: types.Message):
    quote_text = "haloo 👋🏻, bagi kalian yang ingin mengirim pm gunakan :  <blockquote>#boy / #girl</blockquote> kamu juga bisa menggunakan <a href='https://t.me/roleplay_base/665'>AcceptedHashtag</a> jangan lupa taruh username kamu yaa ❕❕"
    await message.reply(text=quote_text, parse_mode=ParseMode.HTML)


from database import *


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False
