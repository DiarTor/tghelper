import telebot
from jdatetime import datetime

from bot.common.fetch_data import get_response_text


class Welcome:
    @staticmethod
    def welcome_new_members(msg: telebot.types.Message, bot: telebot.TeleBot):
        current_time = datetime.now().strftime("%Y/%M/%d - %H:%m:%S")
        for i in msg.new_chat_members:
            bot.send_message(msg.chat.id, get_response_text("welcome.gp", msg.from_user.first_name, msg.from_user.id,
                                                            msg.chat.title, current_time), parse_mode="Markdown")
