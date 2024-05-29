from django.db import models

# Create your models here.

class Upload_img(models.Model):
    name = models.CharField(max_length=10)
    imgfile = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
