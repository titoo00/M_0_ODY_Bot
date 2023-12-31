from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""༫ اهلا بـك عزيـزي 

༫ يمكنك استـخـراج التالـي

༫ تيرمڪس تليثون للحسابات

༫ تيرمـكـس تليثون للبوتـات

༫ بايـروجـرام مـيوزك للحسابات

༫ بايـروجـرام مـيوزك للبوتات

༫ تم انشاء البوت بواسطة [♡ ᎷΌᎠY ♡˼](https://t.me/W_9_N)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إضغط لبدا استخراج الكود", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝐒𝐎𝐔𝐑𝐂𝐄🌐", url="https://t.me/SOURCE_HORSE"),
                    InlineKeyboardButton("♡ ᎷΌᎠY ♡", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
