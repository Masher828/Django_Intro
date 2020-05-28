import os
os.environ['DJANGO_SETTINGS_MODULE']= 'Django_code.settings'

import django
django.setup()

from faker import Faker
import random
from App.models import Topic,Webpage,AccessRecord


fake = Faker()
topics = ["Social", "Marketplace", "Games", "News", "Search"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range (N):
        topic = add_topic()
        url = fake.url()
        date= fake.date()
        company_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic=topic,url=url,name = company_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(25)
    print("Populating Complete ")
