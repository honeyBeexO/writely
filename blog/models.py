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
    date_posted= models.DateTimeField(default=timezone.now)
    date_created= models.DateTimeField(auto_now_add=True)
    # import the user model from django.contrib.auth.models
    author= models.ForeignKey(User, on_delete=models.CASCADE)