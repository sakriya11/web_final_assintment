from django.conf import settings
from django.db import models

# Create your models here.

class galleryUpload(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default="")
    date=models.CharField(max_length=100,default="")
    caption=models.TextField(default="")
    img=models.FileField(blank=True)


