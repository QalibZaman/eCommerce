from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetails(models.Model):

    GENDER_CHOICES = (('M', 'male'),
                     ('F', 'female'))

    name = models.CharField(max_length=250, null=True)
    surname = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, choices=GENDER_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    birthday = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.name + ' '+ self.surname


class Sharing(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    text = models.TextField(null=True)

    def __str__(self) -> str:
        return self.text


class Following(models.Model):
    following = models.ForeignKey(User, on_delete= models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.following.username