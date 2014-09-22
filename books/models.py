from django.db import models
from django.contrib import admin


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    little_image = models.ImageField(upload_to='images/')
    description = models.TextField()

    on_homepage = models.BooleanField(default=False)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name



class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name="authors")
    translators = models.ManyToManyField(Author, null=True, blank=True, related_name="translators")
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    pages = models.PositiveSmallIntegerField()
    ISBN = models.CharField(max_length=20)
    price = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    published = models.BooleanField()
    editors = models.ManyToManyField(Author, null=True, blank=True, related_name="editors")
    cut = models.CharField(max_length="30")
    cover_designer = models.ForeignKey(Author, null=True,blank=True, related_name="cover_designer")

    on_homepage = models.BooleanField(default=False)
    featured_homepage = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

class Edition(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    circulation = models.IntegerField()
    book = models.ForeignKey(Book)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Subject)
admin.site.register(Edition)