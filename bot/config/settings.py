from bot.config.database import settings_col

# default settings
channels_id = ['-1001594818741']
channels_username = ['DiarDev']

if __name__ == "__main__":
    context = {
        "channels_id": [-1001594818741],
        "channels_username": ['DiarDev']
    }
    settings_col.insert_one(context)
