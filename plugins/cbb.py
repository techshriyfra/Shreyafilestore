#(©)MrGhostsx

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴛᴇᴄʜ ꜱʜʀᴇʏᴀɴꜱʜ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Tech_Shreyansh29'>ᴛᴇᴄʜ ꜱʜʀᴇʏᴀɴꜱʜ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/+Q5pbPuc8lGk3YWQ1'>ᴛᴇᴀᴍ ɴᴇᴛғʟɪx</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Tech_Shreyansh2'>ᴛᴇᴄʜ ꜱʜʀᴇʏᴀɴꜱʜ</a>\n○ ɢʀᴏᴜᴘ ᴄʜᴀᴛ : <a href='https://t.me/Tech_Shreyansh2'>ᴛᴇᴄʜ ꜱʜʀᴇʏᴀɴꜱʜ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/Tech_Shreyansh')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
