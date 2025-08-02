from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from info import ADMINS, SUPPORT_CHANNEL
from Script import script

@Client.on_message(filters.private & filters.text & ~filters.command)
async def pm_block_filter(client, message: Message):
    user_id = message.from_user.id

    # If user is an admin, allow filtering
    if user_id in ADMINS:
        return  # do nothing, let the filter plugin work

    # If user is NOT an admin, block and reply with support message
    await message.reply_text(
        text=script.PM_SUPPORT_TXT.format(user=message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton('⤬ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⤬', url=f'http://t.me/{temp.U_NAME}?startgroup=true')],
             [InlineKeyboardButton('🎊 ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ 🎊', url="https://t.me/+RDsxY-lQ55wwOWI1")]
            ]
        )
    )
