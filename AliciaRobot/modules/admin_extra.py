import asyncio

from pyrogram import filters
from pyrogram.types import ChatPermissions

from AliciaRobot import BOT_ID,OWNER_ID, DRAGONS, DEV_USERS, pbot as app
SUDOERS = [OWNER_ID] + DEV_USERS + DRAGONS 


async def member_permissions(chat_id, user_id):
    perms = []
    member = await app.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms



async def current_chat_permissions(chat_id):
    perms = []
    perm = (await app.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_stickers:
        perms.append("can_send_stickers")
    if perm.can_send_animations:
        perms.append("can_send_animations")
    if perm.can_send_games:
        perms.append("can_send_games")
    if perm.can_use_inline_bots:
        perms.append("can_use_inline_bots")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms



@app.on_message(filters.command("fullpromote") & ~filters.edited)
async def promote(_, message):
    try:
        from_user_id = message.from_user.id
        chat_id = message.chat.id
        permissions = await member_permissions(chat_id, from_user_id)
        if "can_promote_members" not in permissions and from_user_id not in SUDOERS:
            await message.reply_text("You don't have enough permissions")
            return
        bot = await app.get_chat_member(chat_id, BOT_ID)
        if len(message.command) == 2:
            username = message.text.split(None, 1)[1]
            user_id = (await app.get_users(username)).id
        elif len(message.command) == 1 and message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            await message.reply_text(
                "Reply To A User's Message Or Give A Username To Promote."
            )
            return
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=bot.can_restrict_members,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await message.reply_text("Promoted successfully!")

    except Exception as e:
        await message.reply_text(str(e))

@app.on_message(filters.command("demote") & ~filters.edited)
async def demote(_, message):
    try:
        from_user_id = message.from_user.id
        chat_id = message.chat.id
        permissions = await member_permissions(chat_id, from_user_id)
        if "can_promote_members" not in permissions and from_user_id not in SUDOERS:
            await message.reply_text("You don't have enough permissions")
            return
        bot = await app.get_chat_member(chat_id, BOT_ID)
        if len(message.command) == 2:
            username = message.text.split(None, 1)[1]
            user_id = (await app.get_users(username)).id
        elif len(message.command) == 1 and message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            await message.reply_text(
                "Reply To A User's Message Or Give A Username To Demote."
            )
            return
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_voice_chats=False,
        )
        await message.reply_text("Demoted successfully!")

    except Exception as e:
        await message.reply_text(str(e))


@app.on_message(filters.command("pin") & ~filters.edited)
async def pin(_, message):
    if not message.reply_to_message:
        await message.reply_text("Reply To A Message To Pin.")
        return
    try:
        from_user_id = message.from_user.id
        chat_id = message.chat.id
        permissions = await member_permissions(chat_id, from_user_id)
        if "can_pin_messages" in permissions or from_user_id in SUDOERS:
            await message.reply_to_message.pin(disable_notification=True)
        else:
            await message.reply_text("You're Not An Admin, Stop Spamming!")
            return
    except Exception as e:
        await message.reply_text(str(e))
