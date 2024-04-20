from faker import Faker
from django.utils import timezone
from django.contrib.auth.models import User

def getRandomPost(n):
    fake = Faker();
    dummy_data = [];
    users = User.objects.all();
    tags = ['Technology','Design','Culture','Business','Politics','Opinion','Science','Health','Style','Travel']
    for i in range(n):
        post = {
            'author':users[i%len(users)],
            'title': fake.sentence(),
            'content': fake.text(),
            'tag':tags[i%len(tags)],
        }
        dummy_data.append(post)
    return dummy_data;
