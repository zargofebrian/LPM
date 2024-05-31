from aiogram import Bot, executor
from aiogram import Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message

PROXY_URL = 'http://proxy.server:3128'

bot = Bot(token="6945981247:AAHuPO0UgNv2z0j3HyW5EpDzFQBurLBFw-w", proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

CHANNEL_ID = -1002079102928

@dp.message_handler(commands=['start'])
async def handler_start(message: types.Message):
    quote_text = "halooo, gimana nih kabarnya ❔ pasti kamu mau kirim menfess ya. <blockquote>Sebelum kirim menfess jangan lupa perhatikan menfes kalian ya apakah sudah sesuai dengan ht dan tidak melanggar rulesnya</blockquote> untuk mengetahui apakah ht kalian sesuai silahkan klik 📂 /hashtag"
    await message.reply(text=quote_text, parse_mode=ParseMode.HTML)

@dp.message_handler(commands=['hashtag'])
async def send_all_hashtags(message: types.Message):
    response = (
        "Berikut adalah penjelasan untuk semua hashtag di channel kami:\n\n"
        "#ELF = untuk bertanya kepada dreamies dan temukan apa yang kalian cari sebagai jawaban di dunia roleplayer ini.\n\n"
        "#FAIRY =  untuk menceritakan pengalaman kalian kepada dreamies tentang dunia roleplayer ini.\n\n"
        "#MERMAID = untuk mencari seseorang yang telah lama di cari seperti teman, pasangan, mutualan channel, akun, dan circle atau paguy..\n\n"
    )
    await message.reply(response)
    await message.answer_sticker('CAACAgUAAxkBAAEL_C9mKf2y-q1CD2_wOxneHKQd5ZUupQACdwwAAuajUFXgkBo0l99wcTQE')


from database import *


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
