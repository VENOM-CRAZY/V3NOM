# COPYRIGHT (C) 2021 @Autichrist

from telethon import events, Button, custom, version
import re, os
from AliciaRobot.events import register
from AliciaRobot import telethn as tbot
from AliciaRobot import (SUPPORT_CHAT, OWNER_USERNAME)

PHOTO = "https://telegra.ph/file/8100710cbc02f7fede30f.jpg"
@register(pattern=("^/alive"))
async def awake(event):
  aliciaXname = event.sender.first_name
  aliciaX = f"Hello {aliciaXname}, I'm Alicia\n\n"
  aliciaX += "♋I'm Working Properly\n\n"
  aliciaX += "♋ Alicia : 3.0 LATEST\n\n"
  aliciaX += f"♋ My Master : [Himanshu](t.me/{OWNER_USERNAME}) ☺️\n\n"
  aliciaX += f"♋ Telethon Version : {version.__version__}\n\n"
  aliciaX += "I'm Happy To Help You! Thanks For Adding Me Here.😊❤️"
  BUTTON = [[Button.url("SUPPORT", f"https://t.me/{SUPPORT_CHAT}"), Button.url("DEVLOPER", f"https://t.me/{OWNER_USERNAME}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=aliciaX,  buttons=BUTTON)


@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aliciaX")))
async def callback_query_handler(event):
# inline by kittu5588 🔥
  himanshu = [[Button.url("REPO", "https://github.com/H1M4N5HU0P/AliciaRobotOP"), Button.url("REPO-USERBOT", "https://github.com/MafiaBotOP/MafiaBot")]]
  himanshu +=[[Button.url("SUPPORT CHANNEL", "https://t.me/MafiaBot_Support"), Button.url("SUPPORT GROUP", "https://t.me/SUPPORT_CHAT")]]
  himanshu +=[[custom.Button.inline("ALIVE", data="himanshu")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=himanshu)

@tbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"himanshu")))
async def callback_query_handler(event):
  global PHOTO
  aliciaXname = event.sender.first_name
  aliciaX = f"Hello {aliciaXname}, I'm Alicia\n\n"
  aliciaX += "♋I'm Working Properly\n\n"
  aliciaX += "♋ Alicia Version : 2.0 LATEST\n\n"
  aliciaX += f"♋ My Master : [Himanshu](t.me/{OWNER_USERNAME}) ☺️\n\n"
  aliciaX += "♋ Telethon Version : 1.19.5\n\n"
  aliciaX += "I'm Happy To Help You! Thanks For Adding Me Here.😊❤️"
  BUTTON = [[Button.url("SUPPORT", f"https://t.me/{SUPPORT_CHAT}"), Button.url("DEVLOPER", f"https://t.me/{OWNER_USERNAME}")]]
  await event.edit(text=aliciaX, buttons=BUTTONS)

__button__ = ""
__buttons__ = ""