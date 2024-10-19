import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'john.settings')

import django
django.setup()

from CRUDApp.models import Employee
from faker import Faker
from random import randint

fake=Faker()
def generatefakedata():
    f_name=fake.name()
    f_age=randint(17, 99)
    f_email=fake.email()
    f_city=fake.city()
    Employee.objects.get_or_create(name=f_name,
                                   age=f_age,
                                   email=f_email,
                                   city=f_city)
for i in range(1,10,1):
    generatefakedata()




