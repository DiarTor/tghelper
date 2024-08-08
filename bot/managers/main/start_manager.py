from telebot import TeleBot
from telebot.types import Message

from bot.config.database import users_col


class StartManager:
    def __init__(self):
        self.welcome_text = "Hi And Welcome {}"

    def start(self, msg: Message, bot: TeleBot) -> Message:
        if not users_col.find_one({'user_id': msg.from_user.id}):
            context = {
                "user_id": msg.from_user.id,
                "username": msg.from_user.username or None,
                "first_name": msg.from_user.first_name or None,
                "last_name": msg.from_user.last_name or None,
                "full_name": f"{msg.from_user.first_name or ""} {msg.from_user.last_name or ""}",
            }
            users_col.insert_one(context)
        return bot.send_message(chat_id=msg.chat.id, text=self.welcome_text.format(msg.from_user.first_name))
