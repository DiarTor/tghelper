import telebot
from jdatetime import datetime
from bot.config.tokens import channels_id


class Welcome:
    def __init__(self):
        self.welcome_message = "Welcome back [{}](tg://user?id={}) ! ⏳{}"

    def welcome_new_members(self, msg: telebot.types.Message, bot: telebot.TeleBot) -> telebot.types.Message:
        current_time = datetime.now().strftime("%Y/%M/%d - %H:%m:%S")
        for i in msg.new_chat_members:
            self.welcome_message = self.welcome_message.format(msg.from_user.first_name, msg.from_user.id, current_time)
            bot.send_message(msg.chat.id, self.welcome_message, parse_mode="Markdown")
