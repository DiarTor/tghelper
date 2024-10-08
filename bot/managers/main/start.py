import telebot.types
from jdatetime import datetime
from telebot import TeleBot
from telebot.types import Message

from bot.common.buttons import ButtonGenerator
from bot.common.control_data import get_response_text, get_settings_data
from bot.common.user_manager import is_private_chat
from bot.config.database import users_col


class StartManager:
    @staticmethod
    def return_to_admin_panel(msg: telebot.types.Message, bot: telebot.TeleBot):
        bot.edit_message_text(text=get_response_text("welcome.admin", msg.from_user.first_name, msg.from_user.id),
                              chat_id=msg.chat.id, message_id=msg.message_id,
                              reply_markup=ButtonGenerator(msg.from_user.id).admin_panel(), parse_mode="markdown")

    @staticmethod
    def insert_user_data(msg: telebot.types.Message):
        context = {
            "user_id": msg.from_user.id,
            "username": msg.from_user.username or None,
            "first_name": msg.from_user.first_name or None,
            "last_name": msg.from_user.last_name or None,
            "full_name": f"{msg.from_user.first_name or ""} {msg.from_user.last_name or ""}",
            "datetime": datetime.now().strftime("%Y/%M/%d - %H:%m:%S"),
            "state": {
                "buttons": ""
            }
        }
        users_col.insert_one(context)

    def start(self, msg: Message, bot: TeleBot) -> Message | None:
        if is_private_chat(msg, bot):
            if not users_col.find_one({'user_id': msg.from_user.id}):
                self.insert_user_data(msg)
            if msg.from_user.id in get_settings_data("admins"):
                return bot.send_message(chat_id=msg.chat.id,
                                        text=get_response_text("welcome.admin", msg.from_user.first_name,
                                                               msg.from_user.id),
                                        reply_markup=ButtonGenerator(msg.from_user.id).admin_panel(),
                                        parse_mode="markdown")
            return bot.send_message(chat_id=msg.chat.id,
                                    text=get_response_text("welcome.pv", msg.from_user.first_name, msg.from_user.id,
                                                           msg.chat.title),
                                    parse_mode='MarkDown')
