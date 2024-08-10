from bot.config.database import settings_col


def get_settings_data(name: str, type: str = "list"):
    try:
        settings_cursor = settings_col.find()
        fields = []
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
