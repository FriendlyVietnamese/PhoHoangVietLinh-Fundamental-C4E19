#tạo 1 file trung gian giữa app và cái database
import mongoengine
#lấy info link này trên mlab(database)
# mongodb://user1:linh99@ds249418.mlab.com:49418/muadongkhonglanh-c4e19
host = "ds249418.mlab.com"
port = 49418
db_name = "muadongkhonglanh-c4e19"
user_name = "user1"
password = "linh99"
#connect tới db
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())