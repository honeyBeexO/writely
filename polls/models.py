from django.db import models # type: ignore
from django.utils import timezone # type: ignore
# Create your models here.
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    
    def was_published_recently(self):
        return self.pub_date>= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return f'{self.id}: {self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.id}: {self.choice_text}'