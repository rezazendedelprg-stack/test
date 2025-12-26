from pyrogram import filters
from bot.casino.slot_machine import handle_casino
from bot.security.anti_login import anti_login_check
from config.config import *

def register_events(app):

    @app.on_message(filters.me)
    async def main_handler(client, message):
        if ANTI_LOGIN_ENABLED:
            await anti_login_check(message)

        await handle_casino(client, message)
