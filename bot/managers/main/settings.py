import telebot.types

from bot.common.buttons import ButtonGenerator
from bot.common.control_data import get_response_text


class GroupSettings:
    @staticmethod
    def show_locker_panel(msg: telebot.types.Message, bot: telebot.TeleBot):
        bot.edit_message_text(text=get_response_text("admin.locker_panel.main"), chat_id=msg.chat.id,
                              message_id=msg.id,
                              reply_markup=ButtonGenerator(msg.from_user.id).locker_panel())

    def show_settings_detail(self, msg: telebot.types.Message, bot: telebot.TeleBot):
        pass
