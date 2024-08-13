from bot.config.database import settings_col
from bot.languages import farsi


def get_settings_data(name: str, type: str = "list"):
    try:
        settings_cursor = settings_col.find()
        fields = []
        if type == "bool":
            return [i.get(name)for i in settings_cursor].pop()
        for settings_doc in settings_cursor:
            fields += settings_doc.get(name, [])
        if type == "list":
            return fields
        elif type == "str":
            return str(''.join(map(str, fields)))
        elif type == "int":
            return int(''.join(map(str, fields)))
    except ValueError as e:
        print(e)


def get_response_text(address: str, *args):
    # Split the text on '.' to access nested dictionary
    keys = address.split('.')
    data = farsi.farsi

    # Traverse the dictionary based on keys
    for key in keys:
        data = data.get(key, {})

    # If data is a string, format it with args if any
    if isinstance(data, str):
        return data.format(*args)
    return None