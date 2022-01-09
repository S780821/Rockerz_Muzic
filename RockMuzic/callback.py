

from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_NAME,
)


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin can tap this button !", show_alert=True)
    await query.edit_message_text(
        "**💡 here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )
    

@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin can tap this button !", show_alert=True)
    await query.edit_message_text(
        f"""📚 **this is the feature information:**
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Command Syntax", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "😕 **couldn't find song you requested**\n\n» **please provide the correct song name or include the artist's name as well**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Command Syntax** to play music on **Voice Chat:**

• `/play (query)` - for playing music via youtube
• `/ytp (query)` - for playing music directly via youtube

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cmdhome")]]
        ),
    )
