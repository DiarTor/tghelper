from bson import ObjectId

from bot.config.database import settings_col

conf_oid = "66bfd1a602804a1672949073"
locker_oid = "66bfd1a602804a1672949074"
dynamic_oid = "66bfd1a602804a1672949075"
# change the default settings as you need.
conf = {
    "admins": [1154909190, 1995271332],
    "channels_id": [-1001594818741],
    "channels_username": ['DiarDev'],
    "group_id": -1002200684633,
    "group_username": "DiarDevGp",
}
locker = {
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
dynamic = {}

if __name__ == "__main__":
    if settings_col.find_one():
        result = settings_col.replace_one({'_id': ObjectId(conf_oid)}, conf)
        settings_col.replace_one({'_id': ObjectId(locker_oid)}, conf)
        settings_col.replace_one({'_id': ObjectId(dynamic_oid)}, conf)
        print(f"Matched Results: {result.matched_count} | Modified Results: {result.modified_count}")
    else:
        settings_col.insert_many([conf, locker, dynamic])
