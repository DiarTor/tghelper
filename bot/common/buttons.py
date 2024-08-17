from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from bot.common.control_data import get_settings_data


class ButtonGenerator:
    def create_reply_keyboard(self, buttons):
        """
        Create ReplyKeyboardMarkup from list of buttons
        :param buttons:
        list of buttons (KeyboardButton)
        :return:
        ReplyKeyboardMarkup object
        """

        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for row in buttons:
            markup.row(*row)
        return markup

    def create_inline_keyboard(self, buttons):
        """
        Create InlineKeyboardMarkup from list of buttons
        :param buttons:
        list of buttons (InlineKeyboardButton)
        :return:
        InlineKeyboardMarkup object
        """

        markup = InlineKeyboardMarkup()
        for row in buttons:
            markup.row(*row)
        return markup

    def admin_panel(self):
        buttons = [[InlineKeyboardButton(text='عضویت اجباری', callback_data='force_join'),
                    InlineKeyboardButton(text='خوش آمد گو', callback_data="welcome")]]
        return self.create_inline_keyboard(buttons)

    def join_channels(self):
        buttons = [[InlineKeyboardButton(text="عضویت در کانال 🔊", url=f"https://t.me/{channel}")] for channel in
                   get_settings_data("channels_username")]
        return self.create_inline_keyboard(buttons)
