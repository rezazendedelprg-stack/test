from pyrogram.types import Message
from utils.logger import logger

async def anti_login_check(message: Message):
    if not message.service:
        return

    text = str(message.service).lower()

    keywords = [
        "login",
        "authorization",
        "new device",
        "logged in"
    ]

    if any(k in text for k in keywords):
        logger.warning("Suspicious login message detected")
        await message.reply(
            "🚨 هشدار: لاگین جدید روی اکانت شناسایی شد"
        )
