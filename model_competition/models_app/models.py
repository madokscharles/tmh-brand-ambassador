# models_app/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return self.user.username
    

class Competition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    

class Entry(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    entry_picture = models.ImageField(upload_to='entry_pictures/')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.profile.user.username} - {self.competition.name}"