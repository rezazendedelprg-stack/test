import asyncio
from pyrogram import Client
from pyrogram.types import Message
from utils.logger import logger

# نگه‌دارنده ست انتخابی
current_target = None

async def handle_casino(client: Client, message: Message):
    global current_target
    text = message.text.lower() if message.text else ""

    # 1️⃣ تنظیم ست در Saved Messages
    if "ست" in text:
        if "۷۷۷" in text or "777" in text:
            current_target = 64
            await message.edit("✅ هدف روی 777 تنظیم شد. حالا در گروه بنویس: ست کازینو")
        elif "bar" in text or "بار" in text:
            current_target = 43
            await message.edit("✅ هدف روی BAR تنظیم شد.")
        elif "لغو" in text:
            current_target = None
            await message.edit("❌ حالت سفارشی لغو شد.")
        return

    # 2️⃣ اجرای دستور در گروه
    if text == "ست کازینو":
        if current_target is None:
            await message.edit(
                "⚠️ اول باید در Saved Messages یک ست انتخاب کنی (مثلاً: ست ۷۷۷)"
            )
            return

        # حذف دستور
        await message.delete()

        logger.info("Casino hunt started")

        while True:
            hunt = await client.send_dice("me", emoji="🎰")

            if hunt.dice.value == current_target:
                await hunt.copy(message.chat.id)
                await client.send_message(
                    "me",
                    f"✅ ست {current_target} با موفقیت به گروه فرستاده شد."
                )
                logger.info("Casino target hit")
                break
            else:
                await hunt.delete()
                await asyncio.sleep(1.5)

