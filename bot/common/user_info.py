import telebot
from bot.config.tokens import channels_id


def is_user_in_channel(user_id, bot: telebot.TeleBot):
    for channels in channels_id:
        member = bot.get_chat_member(channels, user_id)
        return member.status in ['member', 'administrator', 'creator']
