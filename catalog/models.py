from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    
    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} and {self.date_of_death}'
class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    summary = models.TextField()
    isbn  = models.CharField(max_length=16)
    author =  models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Language, null=True,on_delete=models.SET_NULL)

class BookInstance(models.Model):
       uniqueId = models.CharField(max_length=12, unique=True)
       due_back = models.DateField()
       book = models.ForeignKey(Book, on_delete=models.CASCADE)
       imprint = models.TextField()
       borrower = models.ForeignKey(User, null=True,on_delete=models.SET_NULL)
       
       