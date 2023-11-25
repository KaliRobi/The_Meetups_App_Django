from django.db import models

# Create your models here.

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} - {self.address}'


class Meetups(models.Model):
    title = models.CharField(max_length=200)
    meetup_id = models.SlugField(unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True )
    participants = models.ManyToManyField(Participant, blank=True)
    organiser_email = models.EmailField()
    event_date = models.DateField()

    def __str__(self):
        return f'{self.title} - {self.meetup_id}'
    

