from bson import ObjectId

from bot.config.data import toggle_oid
from bot.config.database import settings_col
from bot.languages import farsi


def get_settings_data(name: str = None):
    """
    Retrieves the value associated with the specified name from a MongoDB collection.
    :param name: The name of the key to look for in the documents of the MongoDB collection.
                    If None, the function will attempt to retrieve values but no specific key is targeted.
    :return: The Data of the specified key.
    """
    if name is None:
        raise ValueError("Name parameter cannot be None.")

    document = settings_col.find_one({name: {"$exists": True}}, {name: 1})
    if document and name in document:
        return document[name]
    raise KeyError(f"[{name}] not exists.")


def get_response_text(address: str, *args):
    """
    Retrieves and formats a text string from a nested dictionary based on the given address.
    :param address: A dot-separated string indicating the path to the desired key in the nested dictionary.
    :param args: Additional arguments to format the retrieved string.
    :return: The formatted string if the address leads to a string value, otherwise None.
    """
    keys = address.split('.')
    data = farsi.farsi
    for key in keys:
        if not isinstance(data, dict):
            return None
        data = data.get(key, {})
    if isinstance(data, str):
        return data.format(*args)
    return None


def get_dict(address: str) -> dict:
    """
    Retrieves the dict from the given address
    :param address: The Address of the dict seperated by dots(.)
    :return: Dict
    """
    keys = address.split('.')
    data = farsi.farsi
    for key in keys:
        data = data.get(key)
    return data


def get_all_toggle_settings() -> dict | None:
    """
    Retrieves the toggle settings document from the MongoDB collection.
    :return: The toggle settings document as a dictionary if found, otherwise None.
    """
    try:
        settings_document = settings_col.find_one({'_id': ObjectId(toggle_oid)})
        if settings_document:
            return settings_document
        print("No toggle settings found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def set_filter_data(name: str, value, to) -> bool:
    """
    Updates the value of a specified key in a MongoDB document.
    :param name: The name of the key to look for in the document.
    :param value: The current value of the key to be updated.
    :param to: The new value to set for the specified key.
    :return: True if the update was successful, otherwise False.
    """
    result = settings_col.update_one({name: value}, {"$set": {name: to}})
    return result.modified_count > 0


def toggle_settings_data(name: str) -> bool:
    """
    Toggles the boolean value of a specified key in a MongoDB document.
    :param name: The name of the key whose value is to be toggled.
    :return: The new boolean value after toggling.
    """
    current_value = get_settings_data(name)
    if isinstance(current_value, bool):
        new_value = not current_value
        if set_filter_data(name, current_value, new_value):
            return new_value
        raise RuntimeError(f"Failed to toggle the setting for [{name}].")
    raise ValueError(f"The current value for [{name}] is not a boolean.")
