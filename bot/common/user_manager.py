import telebot
from bot.config.database import settings_col
from bot.common.control_data import get_settings_data
from telebot.apihelper import ApiTelegramException


def is_user_in_channel(user_id, bot: telebot.TeleBot):
    joined_in = 0
    channels = len(get_settings_data("channels_id"))
    for channel_id in get_settings_data("channels_id"):
        try:
            member = bot.get_chat_member(channel_id, user_id)
            if member.status in ['member', 'administrator', 'creator']:
                joined_in += 1
                if joined_in == channels:
                    return True
        except ApiTelegramException:
            print(f"{channel_id} Telegram Chat ID Is Incorrect ")


def is_private_chat(msg: telebot.types.Message, bot: telebot.TeleBot):
    if msg.chat.type != "private":
        bot.reply_to(msg, "please PM me if you want to talk to me :)")
        return False
    return True
