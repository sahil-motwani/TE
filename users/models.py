from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(default='M',max_length=1, choices=GENDER_CHOICES)
    primary_mobile = models.IntegerField(null = True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])
    date_Of_birth = models.DateField(null = True, blank = True)
    
    def __str__(self):
        return '{} Profile'.format(self.user.username)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

