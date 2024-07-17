import pymongo

# server_address
client = pymongo.MongoClient('mongodb://localhost:27017/')

# database
db = client['tghelper']

# collections
users_col = db['users']
