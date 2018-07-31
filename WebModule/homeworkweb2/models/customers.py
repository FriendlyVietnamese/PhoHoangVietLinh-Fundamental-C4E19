from mongoengine import *
class Customers(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()