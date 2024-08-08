from bot.common.user_info import is_user_in_channel
import telebot
from bot.common.buttons import ButtonGenerator

class MessageHandler:
    def __init__(self):
        self.join_channel = 'please join to channel [{}](tg://user?id={}) !'

    def handle_message(self, msg: telebot.types.Message, bot: telebot.TeleBot):
        user_id = msg.from_user.id
        if not is_user_in_channel(user_id, bot):
            self.join_channel = self.join_channel.format(msg.from_user.first_name, user_id)
            bot.send_message(msg.chat.id, self.join_channel, parse_mode='MarkDown', reply_markup=ButtonGenerator().join_channels())
            bot.delete_message(msg.chat.id, msg.id)