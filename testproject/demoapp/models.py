from django.db import models

# Create your models here.

class One(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    image = models.ImageField(upload_to="img/")

    def __str__(self):
        return self.name


class Two(models.Model):
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)