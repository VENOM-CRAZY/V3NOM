from AliciaRobot import pbot as app
from pyrogram import filters
from AliciaRobot.utils.errors import capture_err
import os
import random
from carbonnow import Carbon

async def make_carbon(code):
    carbon = Carbon(code=code)
    image = await carbon.save(str(random.randint(1000, 10000)))
    return image


@app.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        await message.reply_text("Reply to a text message to make carbon.")
        return
    if not message.reply_to_message.text:
        await message.reply_text("Reply to a text message to make carbon.")
        return
    m = await message.reply_text("Preparing Carbon")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading")
    await app.send_photo(message.chat.id, carbon)
    await m.delete()
    os.remove(carbon)