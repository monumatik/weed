from django.db import models

# Create your models here.

class Track(models.Model):
	image = models.ImageField(upload_to='images/')
	YT_Link = models.CharField(max_length=1000)