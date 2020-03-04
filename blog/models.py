from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Code(models.Model):
    code = models.CharField(max_length=255)
    code_means = models.CharField(max_length=255)

class CombinedCodeTable(models.Model):
    combinedcode = models.CharField(max_length=255)
    combinedcode_means = models.CharField(max_length=255)
    description = models.TextField(max_length=600)

class MoodStress(models.Model):
    
    username=models.CharField(max_length=50)
    angry = models.FloatField()
    disgust = models.FloatField()
    fear = models.FloatField()
    happy = models.FloatField()
    neutral = models.FloatField()
    sad = models.FloatField()
    surprise = models.FloatField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('username', 'created')
    def __str__(self):
        return self.username
    