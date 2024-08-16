import telebot

from bot.common.buttons import ButtonGenerator
from bot.common.fetch_data import get_settings_data, get_response_text
from bot.common.user_manager import is_user_in_channel


class MessageHandler:
    @staticmethod
    def handle_message(msg: telebot.types.Message, bot: telebot.TeleBot):
        user_id = msg.from_user.id
        if get_settings_data("force_join", "bool"):
            if not is_user_in_channel(user_id, bot):
                bot.send_message(msg.chat.id,
                                 get_response_text("welcome.force_join", msg.from_user.first_name, msg.from_user.id),
                                 parse_mode='MarkDown',
                                 reply_markup=ButtonGenerator().join_channels())
                bot.delete_message(msg.chat.id, msg.id)
