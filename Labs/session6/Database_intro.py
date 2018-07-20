##Its a place to store your data -NoSQL --> mongodb
from pymongo import MongoClient

URI = "mongodb://user01:linh99@ds229621.mlab.com:29621/c4e19-lab"
#1. Connect với db
client = MongoClient(URI)
#2. Get database
db = client.get_default_database()
#3. Tạo collection
games = db["Games"]
entertainment_links = db["Entertaining links"]
# #4. Tạo Documents
# new_game = {
#     "Name":"Cắt lông mũi",
#     "Describetion":"Funny game",
#     "Type":"Nhảm nhí",
    
# }
# links = {
#     "1":"Google.com",
#     "2":"tumblr.com",
#     "3":"Instagram.com"
# }
# #5. Insert Doc into collection
# games.insert_one(new_game)
# entertainment_links.insert_one(links)
all_games = games.find()
print(all_games[2]["Name"])
