import re
from time import sleep

import requests
from AliciaRobot import TOKEN, dispatcher
from AliciaRobot.modules.helper_funcs.chat_status import (
    is_user_admin,
    user_admin,
)
from AliciaRobot.modules.helper_funcs.filters import CustomFilters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext, CallbackQueryHandler,
    CommandHandler, Filters, MessageHandler, run_async,
)

CHATBOT_ENABLED_CHATS = []

BOT_ID = int(TOKEN.split(":")[0])
AI_API_KEY = 'VVwV177Rz1QOibLD'
AI_BID = 162157


def chatbot_response(query: str, user_id: int) -> str:
    data = requests.get(
        f"http://api.brainshop.ai/get?bid={AI_BID}&"
        + f"key={AI_API_KEY}&uid={user_id}&msg={query}",
    )
    response = data.json()["cnt"]
    return response


def check_message(context: CallbackContext, message):
    reply_msg = message.reply_to_message
    text = message.text
    if re.search("[.|\n]{0,}"+dispatcher.bot.first_name+"[.|\n]{0,}", text, flags=re.IGNORECASE):
        return True
    if reply_msg and reply_msg.from_user.id == BOT_ID:
        return True
    elif message.chat.type == 'privates':
        return True
    else:
        return False



def chatbot(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat_id = update.effective_chat.id
    is_chat = chat_id in CHATBOT_ENABLED_CHATS
    bot = context.bot
    if msg.text and not msg.document:
        if not check_message(context, msg):
            return
        # lower the text to ensure text replace checks
        query = msg.text.lower()
        botname = bot.first_name.lower()
        if botname in query:
            query = query.replace(botname, "bot.name")
        bot.send_chat_action(chat_id, action="typing")
        user_id = update.message.from_user.id
        response = chatbot_response(query, user_id)
        if "Aco" in response:
            response = response.replace("Aco", bot.first_name)
        if "bot.name" in response:
            response = response.replace("bot.name", bot.first_name)
        sleep(0.3)
        msg.reply_text(response, timeout=60)



def list_chatbot_chats(update: Update, context: CallbackContext):
    text = "<b>AI-Enabled Chats</b>\n"
    for chat in CHATBOT_ENABLED_CHATS:
        x = context.bot.get_chat(chat)
        name = x.title or x.first_name
        text += f"??? <code>{name}</code>\n"
    update.effective_message.reply_text(text, parse_mode="HTML")


__help__ = f"""
Chatbot allows {dispatcher.bot.first_name} to talk and provides a more interactive group chat experience.
???
"""

CHATBOT_HANDLER = MessageHandler(Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                                  & ~Filters.regex(r"^s\/")), chatbot)
LIST_CB_CHATS_HANDLER = CommandHandler("listaichats", list_chatbot_chats, filters=CustomFilters.dev_filter)

# Filters for ignoring #note messages, !commands and sed.

dispatcher.add_handler(CHATBOT_HANDLER)
dispatcher.add_handler(LIST_CB_CHATS_HANDLER)

__mod_name__ = "Chatbot"
__command_list__ = ["chatbot", "listaichats"]
__handlers__ = [
    CHATBOT_HANDLER,
    LIST_CB_CHATS_HANDLER,
]
