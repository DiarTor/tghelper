import telebot

from bot.common.buttons import ButtonGenerator
from bot.common.control_data import get_settings_data, get_response_text, toggle_settings_data, get_all_toggle_settings
from bot.common.user_manager import is_user_in_channel


class MessageHandler:
    @staticmethod
    def handle_text_message(msg: telebot.types.Message, bot: telebot.TeleBot):
        user_id = msg.from_user.id
        if get_settings_data("force_join"):
            if not is_user_in_channel(user_id, bot):
                bot.send_message(msg.chat.id,
                                 get_response_text("welcome.force_join", msg.from_user.first_name, msg.from_user.id),
                                 parse_mode='MarkDown',
                                 reply_markup=ButtonGenerator().join_channels())
                bot.delete_message(msg.chat.id, msg.id)

    @staticmethod
    def handle_callback(callback: telebot.types.CallbackQuery, bot: telebot.TeleBot):
        data = callback.data
        if data in list(get_all_toggle_settings()):
            toggle_settings_data(data)
