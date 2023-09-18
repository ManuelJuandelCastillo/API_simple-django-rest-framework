from django.db import models

# Create your models here.


class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    is_adtive = models.BooleanField(default=True)
