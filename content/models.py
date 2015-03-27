from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=200)
    tags = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    abstract = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    links = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=50)
    contents = models.ManyToManyField(Content, null=True, blank=True)

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

