from django.contrib.auth.models import User
from django.db import models
from django.template.context_processors import request



class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name


class UserPersona(models.Model):
    name = models.CharField(max_length=64,unique=True)
    normalized_name=models.CharField(max_length=64,unique=True)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    #owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    full_name = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    #settings
    is_full_name_displayed = models.BooleanField(default=True)


    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200,blank=True, null=True)
    persona=models.ForeignKey(UserPersona,on_delete=models.SET_NULL,blank=True, null=True)
    interests = models.ManyToManyField(UserInterest,blank=True)

    def __str__(self):
        return self.user.username
