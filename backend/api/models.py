from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Place(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    postal_code = models.IntegerField()
    locality = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name 
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')
    rating = models.FloatField()

    def __str__(self):
        return f'{self.rated_by.username} rated {self.user.username} {self.rating}'