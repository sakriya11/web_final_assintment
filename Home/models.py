from django.conf import settings
from django.db import models


# Create your models here.
class slider(models.Model):
    img = models.FileField(upload_to='assets')
    title = models.CharField(max_length=100)

class service(models.Model):
    title= models.CharField(max_length=100)
    text= models.TextField()

class testimonials(models.Model):
    img = models.FileField(upload_to='assets')
    desc = models.TextField()
    name = models.CharField(max_length=100)

class photoupload(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo=models.FileField(blank=True)
    caption=models.TextField()
    caption_title=models.CharField(max_length=100)

class news(models.Model):
    Name =models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Telephone=models.CharField(max_length=20)
    Subject=models.CharField(max_length=50)
    Message=models.CharField(max_length=100)

