#thư viện
from pymongo import MongoClient
#URI của database-> get database
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
#kết nối vô uri đó bằng lệnh MongoClient(uri)
client = MongoClient(uri)
#lấy kho dữ liệu của mục posts
db = client.get_default_database()
posts = db["posts"]

#tạo post
post = {"title":"Thơ con cóc",
        "author":"ViLinh",
        "content":"Roses are red\nViolets are blue\nI hope that you met\nSomeone fuck you like I do"
}
posts.insert_one(post)
print("Done!")