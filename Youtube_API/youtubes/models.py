from django.db import models

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=100)
    comment = models.TextField(max_length=500)
    likes = models.IntegerField(default=0, null=False)
    dislikes = models.IntegerField(default=0, null=False)

class Reply (models.Model):
    comment = models.ForeignKey(Comment,  on_delete=models.CASCADE)
    reply = models.TextField(max_length=500)


    def __str__(self):
        return self.title