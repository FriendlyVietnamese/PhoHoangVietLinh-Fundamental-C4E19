from models.service import Service,so_do
import mlab
from faker import Faker
from random import randint,choices
##mlab là để kết nổi database
#faker providers
##https://faker.readthedocs.io/en/master/providers.html
fake = Faker()
mlab.connect()
images = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTURgyIsyjuJ4I0wyw0vQK7PEH3zluq_2mJQNH2SrT_HwSqnDQU",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGDh5vIJ1hj-nf4OogDGPIQKxnD9XBa_y0g4OJhvJWZGwhNQNU",
        "https://s3.bloganchoi.com/wp-content/uploads/2017/07/girlsday-hyeri.jpg",
        "https://i.pinimg.com/736x/93/12/be/9312beb33781b88ae6b4a39a530988e9.jpg",
        "http://cdn.hoahoctro.vn/uploads/2017/11/5a085bb27feff-unnamed-8.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbinQR5q8_hFBFLIJ2nCvwpLdp3c3sIaionFwbQTi3TKlP2ns3VA",
        "https://i.pinimg.com/originals/32/74/75/3274754039c877fd961cef6d57955616.jpg"
        ]
for i in range(7):
    v1 = randint(80,105)
    v2 = randint(55,70)
    v3 = randint(80,105)
    hobby = ["ngoan hiền","dễ thương","nghe lời","bị les","thân thiện","lễ phép", "chiều chồng","biết cưỡi ngựa","gầm cao vó dài","bị sida","ngon nghẻ trắng trẻo"]
    hobby = choices(hobby, k=3)
    describe = ", ".join(hobby)
    new_service = Service(
        image = images[i],
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