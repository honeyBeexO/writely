from faker import Faker

def getRandomPost():
    fake = Faker();
    dummy_data = [];
    tags = ['Technology','Design','Culture','Business','Politics','Opinion','Science','Health','Style','Travel']
    for i in range(20):
        post = {
            'author':fake.name(),
            'title': fake.sentence(),
            'content': fake.text(),
            'date_posted': fake.date(),
            'tag':tags[i%len(tags)],
        }
        dummy_data.append(post)
    return dummy_data;
