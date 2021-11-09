from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    posted_date = models.CharField(max_length=50)
    comments = []


    def __str__(self):
        return self.title