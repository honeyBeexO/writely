from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    # We can use auto_now_add=True but that means we set
    # the date only when this object is created once and it's final. that would be better for date created
    # instead we can use default with a django utility Timezone. now we can update the date later on
    date_posted= models.DateTimeField(default=timezone.now, null=True,blank=True)
    date_created= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # import the user model from django.contrib.auth.models
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #Querying use: .filter()| .get() returns a single value or error| .all() returns a set or QuerySet
    #Querying use: .save() to write the python object into the database
    #Querying use: user.modelName_set.. to do many things, it gives us something to query against
    # when querying we can find all the posts created by this user using the: user.post_set.all() | user.post_set.create(post)

    def __str__(self):
        return f'{self.title} By {self.author.username}';