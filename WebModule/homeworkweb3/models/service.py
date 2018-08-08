##design database
#http://docs.mongoengine.org/guide/defining-documents.html#fields
from mongoengine import *
from random import choices,randint
def so_do(a,b,c):
    return "{0} - {1} - {2}".format(a,b,c)
def describe(a,b,c):
    return "{0}, {1}, {2}".format(a,b,c)

class Service(Document):
    image = StringField()
    name = StringField()
    yob = IntField()
    gender = IntField()
    phone = StringField()
    height = IntField()
    address = StringField()
    describe = StringField()
    info = StringField()

    

# new_service = Service(
#     name = "Phó Hoàng Việt Linh",
#     yob = 1999,
#     gender = 1,
#     height = 168,
#     phone = "01234567890",
#     address = "HN",
#     status = True
# )

# new_service.save()