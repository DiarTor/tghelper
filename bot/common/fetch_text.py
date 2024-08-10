from bot.languages import farsi


def get_response_text(text: str, *args):
    # Split the text on '.' to access nested dictionary
    keys = text.split('.')
    data = farsi.farsi

    # Traverse the dictionary based on keys
    for key in keys:
        data = data.get(key, {})

    # If data is a string, format it with args if any
    if isinstance(data, str):
        return data.format(*args)
    return None
