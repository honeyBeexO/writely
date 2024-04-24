from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
# Create your models here.


class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    summary = models.TextField()
    isbn = models.CharField(max_length=16)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(
        Language, null=True, on_delete=models.SET_NULL)
    # Metadata

    class Meta:
        ordering = ['-title']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name


class BookInstance(models.Model):
    LOAN_STATUS = [
        ('ON','ON LOAN'),
    ]
    uniqueId = models.CharField(max_length=12, unique=True)
    due_back = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.TextField()
    borrower = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


# class GenreBook(models.Model):
#     genre = models.OneToOneField(Genre, on_delete=models.CASCADE)
#     book = models.OneToOneField(Book, on_delete=models.CASCADE)
