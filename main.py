import logging
import os

import telebot
from dotenv import load_dotenv

from bot.managers.group.welcome import Welcome
from bot.managers.main.message import MessageHandler
from bot.managers.main.start import StartManager

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# config
load_dotenv()
bot = telebot.TeleBot(token=os.getenv('BOT_TOKEN'), disable_web_page_preview=True)
telebot.apihelper.API_URL = "http://localhost:8081/bot{0}/{1}"
# managers
bot.register_message_handler(StartManager().start, commands=['start'], pass_bot=True)
bot.register_message_handler(Welcome().welcome_new_members, content_types=['new_chat_members'], pass_bot=True)
bot.register_message_handler(MessageHandler().handle_text_message, content_types=['text'], pass_bot=True)
bot.register_callback_query_handler(MessageHandler().handle_callback, pass_bot=True, func=lambda call: True)
# starter
if __name__ == "__main__":
    try:
        logger.info("Starting bot polling")
        # test = bot.log_out()
        # print(test)
        bot.infinity_polling()
    except Exception as e:
        logger.error("An error occurred: %s", e)
        raise
