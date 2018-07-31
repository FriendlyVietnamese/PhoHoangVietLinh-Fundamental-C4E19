from models.customers import Customers
import mlab
from faker import Faker
from random import randint,choice

##https://faker.readthedocs.io/en/master/providers.html
fake = Faker()
mlab.connect()
for i in range(50):
    new_customer = Customers(
        name = fake.name(),
        gender = randint(0,1),
        company = fake.address(),
        job = fake.job(),
        email = fake.email(),
        contacted = choice([True,False])
    )
    new_customer.save()
    print("Uploading", i+1,"....")