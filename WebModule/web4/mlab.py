import mongoengine
host = "ds215172.mlab.com"
port = 15172
db_name = "youtube_demo"
user_name = "user01"
password = "linh99"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())