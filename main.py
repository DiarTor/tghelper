import logging

import telebot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
bot = telebot.TeleBot(token="6545347914:AAF0-kxh-8Ztn8JNXTCkmiumfdR3Z7K8vKs", parse_mode="markdown")

if __name__ == "__main__":
    try:
        logger.info("Starting bot polling")
        bot.infinity_polling()
    except Exception as e:
        logger.error("An error occurred: %s", e)
        raise
