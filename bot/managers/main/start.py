import telebot.types
from telebot import TeleBot
from telebot.types import Message
from jdatetime import datetime
from bot.config.database import users_col
from bot.common.user_manager import is_private_chat


class StartManager:
    def __init__(self):
        self.welcome_message = "Welcome [{}](tg://user?id={}) !"

    @staticmethod
    def insert_user_data(msg: telebot.types.Message):
        context = {
            "user_id": msg.from_user.id,
            "username": msg.from_user.username or None,
            "first_name": msg.from_user.first_name or None,
            "last_name": msg.from_user.last_name or None,
            "full_name": f"{msg.from_user.first_name or ""} {msg.from_user.last_name or ""}",
            "datetime": datetime.now().strftime("%Y/%M/%d - %H:%m:%S")
        }
        users_col.insert_one(context)

    def start(self, msg: Message, bot: TeleBot) -> Message | None:
        if is_private_chat(msg, bot):
            if not users_col.find_one({'user_id': msg.from_user.id}):
                self.insert_user_data(msg)
            return bot.send_message(chat_id=msg.chat.id,
                                    text=self.welcome_message.format(msg.from_user.first_name, msg.from_user.id),
                                    parse_mode='MarkDown')