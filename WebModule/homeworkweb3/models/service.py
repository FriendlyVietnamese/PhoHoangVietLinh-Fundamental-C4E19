##design database
#http://docs.mongoengine.org/guide/defining-documents.html#fields
from mongoengine import *
import datetime

def so_do(a,b,c):
    return "{0} - {1} - {2}".format(a,b,c)
def describe(a,b,c):
    return "{0}, {1}, {2}".format(a,b,c)

class Service(Document):
    image = StringField(required = True)
    name = StringField(required = True)
    yob = IntField(required = True)
    gender = IntField(required = True)
    phone = StringField(required = True)
    height = IntField(required = True)
    address = StringField(required = True)
    describe = StringField(required = True)
    info = StringField(required = True)
class User(Document):
    name = StringField(required = True)
    email = StringField(required = True)
    user = StringField(required = True)
    password = StringField(required = True)
class Order(Document):
    
    service_id = ReferenceField(Service)
    user_id = ReferenceField(User)
    is_accepted = BooleanField(default= datetime.datetime.now)
    time = DateTimeField(default= False)
    
    

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