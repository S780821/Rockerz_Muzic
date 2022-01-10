import requests
from pytgcalls import idle
from callsmusic import run
from RockMuzic import __version__
from pyrogram import Client as Bot
from config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN


response = requests.get(BG_IMAGE)
with open("./ImageFont/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="RockMuzic"),
)

print(f"[INFO]: ROCKERZ MUZIC v{__version__} STARTED !")

bot.start()
run()
idle()
