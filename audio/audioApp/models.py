from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.

class Song(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Podcast(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100, null=False)
    participants = PickledObjectField(default=list())

    def __str__(self):
        return self.name + '-' + self.host

class AudioBook(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    narrator = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    upload_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + '-' + self.author + '-' + self.narrator




