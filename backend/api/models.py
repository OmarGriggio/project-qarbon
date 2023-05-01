from django.db import models

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
    # place = reference dans une autre table
    price = models.DecimalField(decimal_places=2, max_digits=5)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name 
    

