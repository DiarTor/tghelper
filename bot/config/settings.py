from bot.config.database import settings_col

# change the default settings as you need.

if __name__ == "__main__":
    context = {
        "channels_id": [-1001594818741],
        "channels_username": ['DiarDev'],
        "group_id": -1002200684633,
        "group_username": "DiarDevGp",
        "force_join": False,
        "welcome": True,
        "force_add": False,
        "lock_hashtag": False,
        "lock_username": False,
        "lock_link": False,
        "lock_tg_service": True,
        "lock_caption": False,
        "lock_inline": False,
        "lock_bot": True,
        "lock_picture": False,
        "lock_forward": False,
        "lock_gif": False,
        "lock_sticker": False,
        "lock_file": False,
        "lock_contact": True,
        "lock_location": True,
        "lock_command": False,
        "lock_pin": True,
        "lock_video": True,
        "lock_video_note": True,
        "lock_audio": False,
        "lock_voice": False,

    }
    settings_col.insert_one(context)
