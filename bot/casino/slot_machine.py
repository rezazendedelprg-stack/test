from pyrogram import filters
import asyncio
import logging

current_target = None

@app.on_message(filters.me & filters.text)
async def casino_controller(client, message):
    global current_target

    text = message.text.lower().strip() if message.text else ""

    logger.info(
        f"MSG | chat_id={message.chat.id} | type={message.chat.type} | text='{text}'"
    )

    # ==================================
    # 1️⃣ Saved Messages - تنظیم ست
    # ==================================
    if message.chat.is_self:
        logger.info("Saved Messages detected")

        if "ست" in text:
            if "777" in text or "۷۷۷" in text:
                current_target = 64
                logger.info("Target set to 777 (64)")
                await message.edit("✅ هدف روی 777 تنظیم شد")

            elif "bar" in text or "بار" in text:
                current_target = 43
                logger.info("Target set to BAR (43)")
                await message.edit("✅ هدف روی BAR تنظیم شد")

            elif "لغو" in text:
                current_target = None
                logger.info("Target cleared")
                await message.edit("❌ ست لغو شد")
        else:
            logger.debug("Saved message ignored (no command)")
        return

    # ==================================
    # 2️⃣ Group - اجرای کازینو
    # ==================================
    if "ست کازینو" in text:
        logger.info("Casino command received in group")

        if current_target is None:
            logger.warning("Command received but target is None")
            await message.edit("⚠️ اول در سیو مسیج ست رو انتخاب کن")
            return

        await message.delete()
        logger.info("Command message deleted")

        while True:
            logger.debug("Sending 🎰 to Saved Messages")
            hunt = await client.send_dice("me", emoji="🎰")

            if hunt.dice.value == current_target:
                logger.info(
                    f"Target hit! value={hunt.dice.value} | sending to group"
                )
                await hunt.copy(message.chat.id)

                await client.send_message(
                    "me",
                    f"✅ ست {current_target} با موفقیت ارسال شد"
                )
                break
            else:
                logger.debug(
                    f"Missed value={hunt.dice.value} | retrying..."
                )
                await hunt.delete()
                await asyncio.sleep(1.5)

    else:
        logger.debug("Group message ignored (not casino command)")

