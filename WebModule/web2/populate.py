from models.service import Service
import mlab
from faker import Faker
from random import randint,choice
##mlab là để kết nổi database
#faker providers
##https://faker.readthedocs.io/en/master/providers.html
fake = Faker()
mlab.connect()
for i in range(20):
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = choice([0,1]),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True,False])
    )
    new_service.save()