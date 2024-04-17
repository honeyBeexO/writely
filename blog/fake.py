from faker import Faker

def getRandomPost():
    fake = Faker();
    dummy_data = [];
    for i in range(10):
        post = {
            'author':fake.name(),
            'title': fake.sentence(),
            'content': fake.text(),
            'date_posted': fake.date(),
        }
        dummy_data.append(post)
    return dummy_data;
