import os
os.environ['DJANGO_SETTINGS_MODULE']= 'Project.settings'
import django
django.setup()
from faker import Faker
from registration_form.models import user_details
fake = Faker()
def add_user(N=5):
    for i in range(N):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        t = user_details.objects.get_or_create(first_name= first_name,last_name=last_name,email=email)[0]

if __name__ == '__main__':
    add_user(20)
