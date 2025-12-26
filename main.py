from bot.client import create_client
from bot.events import register_events
from utils.logger import logger

app = create_client()
register_events(app)

logger.info("Casino Userbot started")

app.run()
