from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='./pics')
    desc=models.TextField()

    def __str__(self) -> str:
        return self.name

class review(models.Model):
    pic=models.ImageField(upload_to='profile')
    pname=models.CharField(max_length=100)
    about=models.TextField()

    def __str__(self) -> str:
        return self.pname