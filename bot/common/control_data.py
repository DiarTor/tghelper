from bson import ObjectId

from bot.config.data import toggle_oid
from bot.config.database import settings_col
from bot.languages import farsi


def get_filter_data(name: str = None):
    settings_cursor = settings_col.find()
    value = None
    for dt in [i for i in settings_cursor]:
        try:
            value = dt[name]
            return value
        except KeyError:
            continue

    if value is None:
        raise KeyError(f"[{name}] not exists.")


def get_all_toggle_settings() -> dict | None:
    try:
        # Query to find the document with the given settings_oid
        settings_document = settings_col.find_one({'_id': ObjectId(toggle_oid)})
        if settings_document:
            return settings_document
        else:
            print("No toggle settings found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_response_text(address: str, *args):
    keys = address.split('.')
    data = farsi.farsi
    for key in keys:
        data = data.get(key, {})
    if isinstance(data, str):
        return data.format(*args)
    return None



def set_filter_data(name: str, value, to):
    document = settings_col.find_one({name: value})
    if document:
        settings_col.update_one({name: value}, {"$set": {name: to}})


def toggle_settings_data(name: str):
    current_value = get_filter_data(name)
    set_filter_data(name, current_value, not current_value)
    return not current_value
