from models.service import Service,so_do
import mlab
from faker import Faker
from random import randint,choices
##mlab là để kết nổi database
#faker providers
##https://faker.readthedocs.io/en/master/providers.html
fake = Faker()
mlab.connect()

for i in range(7):
    v1 = randint(80,105)
    v2 = randint(55,70)
    v3 = randint(80,105)
    hobby = ["ngoan hiền","dễ thương","nghe lời","bị les","thân thiện","lễ phép", "chiều chồng","biết cưỡi ngựa","gầm cao vó dài","bị sida","ngon nghẻ trắng trẻo"]
    hobby = choices(hobby, k=3)
    describe = ", ".join(hobby)

    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        describe = describe,
        info = so_do(v1,v2,v3)
    )
    new_service.save()
    print(i+1)