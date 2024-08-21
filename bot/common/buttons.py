from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from bot.common.control_data import get_settings_data
from bot.config.database import users_col
from bot.languages import english


class ButtonGenerator:
    def __init__(self, user_id):
        self.user_id = user_id

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

    def save_previous_state(self, state):
        """
        Save the state of buttons in the user's document.
        Convert InlineKeyboardButton objects to dictionaries before saving.
        """
        users_col.update_one(
            {'user_id': self.user_id},
            {'$set': {'state.buttons': state}},
            upsert=True
        )

    def return_button(self):
        """
        Create a return button that loads the previous state from the user's document.
        """
        user_data = users_col.find_one({'user_id': self.user_id})
        to = user_data['state']['buttons']
        return [[InlineKeyboardButton(text='• RETURN •', callback_data=to)]]

    def admin_panel(self):
        buttons = [[InlineKeyboardButton(text="• Manage Lockers •", callback_data="locker_panel")]]
        return self.create_inline_keyboard(buttons)

    def locker_panel(self):
        buttons = []
        for key, text in english.english['translations']['lockers'].items():
            emoji = '🔒' if get_settings_data(key) else '🔓'
            buttons.append(InlineKeyboardButton(text=f"{emoji} {text}", callback_data=f"{key}"))

        # Group buttons into rows of 2
        rows = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
        self.save_previous_state("admin_panel")
        rows += self.return_button()
        return self.create_inline_keyboard(rows)

    def join_channels(self):
        buttons = [[InlineKeyboardButton(text="Join Channel 🔊", url=f"https://t.me/{channel}")] for channel in
                   get_settings_data("channels_username")]
        return self.create_inline_keyboard(buttons)
