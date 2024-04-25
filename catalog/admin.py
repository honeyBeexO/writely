from django.contrib import admin
from catalog import models
# Register your models here.
admin.site.register(models.Genre)
admin.site.register(models.Language)

#admin.site.register(models.Book)
#admin.site.register(models.BookInstance)

#admin.site.register(models.Author)
@admin.register(models.Book) # this the same as: admin.site.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )