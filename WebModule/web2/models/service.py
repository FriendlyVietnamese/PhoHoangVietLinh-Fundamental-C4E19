##design database
#http://docs.mongoengine.org/guide/defining-documents.html#fields
from mongoengine import *
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()


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