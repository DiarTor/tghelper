import telebot
from bot.config.database import settings_col
from bot.common.fetch_data import get_settings_data
from telebot.apihelper import ApiTelegramException


def is_user_in_channel(user_id, bot: telebot.TeleBot):
    for channel_id in get_settings_data("channels_id"):
        # Check if the user is a member, administrator, or creator
        try:
            member = bot.get_chat_member(channel_id, user_id)
            if member.status in ['member', 'administrator', 'creator']:
                return True
        except ApiTelegramException:
            print(f"{channel_id} Telegram Chat ID Is Incorrect ")
